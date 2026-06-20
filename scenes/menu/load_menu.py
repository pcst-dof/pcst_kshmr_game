import os
import pygame
from scenes.menu.main_menu import BASE_DIR
from scenes.scene import Scene
from ui.button import Button
from ui.save_slot import SaveSlot  # NEW
from ui.dialogs import ConfirmationDialog  # NEW
from utils.save_manager import SaveManager  # NEW

MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40

class LoadMenu(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.png')
        self.game = game
        self.save_manager = SaveManager()  # NEW: инициализируем менеджер
        self.set_text("Load Game")
        
        # NEW: Навигация по страницам
        self.current_page = 0
        self.slots_per_page = 6
        self.save_slots = []
        
        # NEW: Диалог подтверждения
        self.confirmation_dialog = None
        self.pending_load_slot = None
        
        self.create_ui()
        self.refresh_slots()  # NEW: загружаем слоты
    
    def create_ui(self):
        # Кнопка "Вернуться"
        button_width = 260
        button_height = 56
        button_x = (self.game.LOGICAL_W - button_width) // 2
        button_y = self.game.LOGICAL_H - 130

        back_btn = Button(
            button_x,
            button_y,
            button_width,
            button_height,
            "Вернуться",
            (100, 100, 255),
            (255, 255, 255),
            lambda: self.game.change_scene("main_menu"),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE
        )
        self.add_button(back_btn)
        
        # NEW: Кнопки навигации < >
        nav_y = self.game.LOGICAL_H - 200
        self.prev_page_btn = Button(
            100, nav_y, 60, 50, "<", (80, 80, 80), (200, 200, 200),
            self.prev_page, font_path=MY_FONT_PATH, font_size=30
        )
        self.next_page_btn = Button(
            self.game.LOGICAL_W - 160, nav_y, 60, 50, ">", (80, 80, 80), (200, 200, 200),
            self.next_page, font_path=MY_FONT_PATH, font_size=30
        )
        self.add_button(self.prev_page_btn)
        self.add_button(self.next_page_btn)
    
    def refresh_slots(self):
        """NEW: Обновить список слотов сохранений"""
        self.save_slots.clear()
        saves = self.save_manager.get_all_saves()
        
        # Позиции слотов (сетка 3x2)
        slot_width = 350
        slot_height = 250
        start_x = 150
        start_y = 150
        
        # Показываем только слоты текущей страницы
        start_idx = self.current_page * self.slots_per_page
        end_idx = start_idx + self.slots_per_page
        
        for idx, (slot_num, save_info) in enumerate(saves[start_idx:end_idx]):
            x = start_x + (idx % 3) * (slot_width + 30)
            y = start_y + (idx // 3) * (slot_height + 30)
            
            save_slot = SaveSlot(x, y, slot_width, slot_height, slot_num, save_info)
            self.save_slots.append(save_slot)
    
    def prev_page(self):
        """NEW: Предыдущая страница"""
        if self.current_page > 0:
            self.current_page -= 1
            self.refresh_slots()
    
    def next_page(self):
        """NEW: Следующая страница"""
        total_pages = (len(self.save_manager.get_all_saves()) + self.slots_per_page - 1) // self.slots_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.refresh_slots()
    
    def attempt_load(self, slot):
        """NEW: Попытка загрузить сохранение (показываем диалог)"""
        save_info = self.save_manager.get_save_info(slot)
        
        if not save_info:
            print(f"No save in slot {slot}")
            return
        
        # Показываем диалог подтверждения
        self.pending_load_slot = slot
        self.confirmation_dialog = ConfirmationDialog(
            self.game.screen,
            "Loading will lose unsaved progress.\nAre you sure you want to do this?",
            self.confirm_load,
            self.cancel_load
        )
    
    def confirm_load(self):
        """NEW: Подтвердить загрузку"""
        if self.pending_load_slot is not None:
            game_state = self.save_manager.load_save(self.pending_load_slot)
            if game_state:
                # Загружаем состояние в игру
                self.game.load_state(game_state)
                # Переходим к сцене из сохранения
                scene_name = game_state.get('current_scene', 'main_menu')
                self.game.change_scene(scene_name)
        
        self.pending_load_slot = None
        self.confirmation_dialog = None
    
    def cancel_load(self):
        """NEW: Отменить загрузку"""
        self.pending_load_slot = None
        self.confirmation_dialog = None
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        # Если активен диалог - обрабатываем только его
        if self.confirmation_dialog:
            return self.confirmation_dialog.handle_event(event)

        # Обработка кликов мыши: используем virtual mouse pos, если он передан
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None:
                # Проверяем клики по слотам
                for slot in self.save_slots:
                    if slot.rect.collidepoint(click_pos):
                        self.attempt_load(slot.slot_number)
                        return True

                # Проверяем кнопки
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True

        # Клавиатурная обработка: ESC возвращает на главное меню
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_scene("main_menu")
                return True

        return False
    
    def update(self, dt):
        if self.confirmation_dialog:
            return
        
        # Обновляем состояние слотов
        mouse_pos = pygame.mouse.get_pos()
        for slot in self.save_slots:
            slot.hovered = slot.rect.collidepoint(mouse_pos)
    
    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)
        
        # Рисуем слоты
        for slot in self.save_slots:
            slot.draw(screen)
        
        # Рисуем диалог если есть
        if self.confirmation_dialog:
            self.confirmation_dialog.draw()