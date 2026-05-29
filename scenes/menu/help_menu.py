# scenes/menu/help_menu.py
import os
import pygame
from scenes.menu.main_menu import BASE_DIR
from scenes.scene import Scene
from ui.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40
SMALL_FONT_SIZE = 24


class HoverButton(Button):
    """Кнопка с активным состоянием (для вкладок)"""
    def __init__(self, x, y, width, height, text, 
                 color, hover_color, text_color, 
                 action=None, font_path=None, font_size=36):
        super().__init__(x, y, width, height, text, color, text_color, 
                        action, font_path, font_size)
        self.hover_color = hover_color
        self.original_color = color
        self.active = False 
    
    def draw(self, screen, mouse_pos):
        hovered = mouse_pos is not None and self.rect.collidepoint(mouse_pos)
        
        if self.active:
            self.accent_color = self.hover_color
        elif hovered:
            self.accent_color = self.hover_color 
        else:
            self.accent_color = self.original_color
        
        pygame.draw.rect(screen, self.accent_color, self.rect, border_radius=12)
        super().draw(screen, mouse_pos)


class HelpMenu(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.png')
        self.game = game
        self.set_text("Справка")
        
        self.keyboard_controls = [
            ("Enter", "Продвигает диалог и активирует интерфейс."),
            ("Space", "Продвигает диалог без выбора вариантов."),
            ("Стрелки", "Навигация по интерфейсу."),
            ("Escape", "Открывает игровое меню."),
            ("Ctrl", "Пропускает диалог при удержании."),
            ("Tab", "Переключает пропуск диалога."),
            ("Page Up", "Возвращается к предыдущему диалогу."),
            ("Page Down", "Переходит к следующему диалогу."),
            ("H", "Скрывает пользовательский интерфейс."),
            ("S", "Делает скриншот."),
            ("V", "Переключает автоматическое озвучивание."),
            ("Shift+A", "Открывает меню специальных возможностей."),
        ]
        
        self.mouse_controls = [
            ("ЛКМ", "Продвигает диалог и активирует интерфейс."),
            ("СКМ", "Скрывает пользовательский интерфейс."),
            ("ПКМ", "Открывает игровое меню."),
            ("Колёсико вверх", "Возвращается к предыдущему диалогу."),
            ("Колёсико вниз", "Переходит к следующему диалогу."),
        ]
        
        self.title_font = pygame.font.Font(MY_FONT_PATH, MY_FONT_SIZE)
        self.small_font = pygame.font.Font(MY_FONT_PATH, SMALL_FONT_SIZE)
        
        self.start_y = 180
        self.line_height = 45
        self.content_x = 200
        self.key_column_width = 220
        
        button_width = 280
        button_height = 50
        button_y = 80
        spacing = 20
        
        total_width = (button_width * 2) + spacing
        start_x = (self.game.LOGICAL_W - total_width) // 2
        
        self.keyboard_btn = HoverButton(
            start_x, button_y, button_width, button_height,
            "Клавиатура", (70, 70, 130), (100, 100, 180), (255, 255, 255),
            lambda: self.set_view('keyboard'),
            font_path=MY_FONT_PATH, font_size=28
        )
        self.keyboard_btn.active = True
        
        self.mouse_btn = HoverButton(
            start_x + button_width + spacing, button_y, button_width, button_height,
            "Мышь", (70, 70, 130), (100, 100, 180), (255, 255, 255),
            lambda: self.set_view('mouse'),
            font_path=MY_FONT_PATH, font_size=28
        )
        
        self.add_button(self.keyboard_btn)
        self.add_button(self.mouse_btn)
        
        self.current_view = 'keyboard'
        
        back_button_width = 260
        back_button_height = 56
        back_button_x = (self.game.LOGICAL_W - back_button_width) // 2
        back_button_y = self.game.LOGICAL_H - 130

        back_btn = Button(
            back_button_x, back_button_y, back_button_width, back_button_height,
            "Вернуться", (100, 100, 255), (255, 255, 255),
            lambda: game.change_scene("main_menu"),
            font_path=MY_FONT_PATH, font_size=MY_FONT_SIZE 
        )
        self.add_button(back_btn)
    
    def set_view(self, view):
        """Переключение между видами"""
        self.current_view = view
        self.keyboard_btn.active = (view == 'keyboard')
        self.mouse_btn.active = (view == 'mouse')
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """Обработка событий — ВНУТРИ класса, без btn.handle_event()"""
        
        # Подсветка активной вкладки (визуал)
        if mouse_pos:
            if self.keyboard_btn.rect.collidepoint(mouse_pos):
                self.keyboard_btn.accent_color = self.keyboard_btn.hover_color
            else:
                if self.current_view == 'keyboard':
                    self.keyboard_btn.accent_color = (120, 120, 200)
                else:
                    self.keyboard_btn.accent_color = self.keyboard_btn.original_color
            
            if self.mouse_btn.rect.collidepoint(mouse_pos):
                self.mouse_btn.accent_color = self.mouse_btn.hover_color
            else:
                if self.current_view == 'mouse':
                    self.mouse_btn.accent_color = (120, 120, 200)
                else:
                    self.mouse_btn.accent_color = self.mouse_btn.original_color
        
        # Базовый класс обработает клики по кнопкам через is_clicked()
        return super().handle_event(event, mouse_pos, action, dt)
    
    def draw(self, surface, mouse_pos=None):
        """Отрисовка сцены"""
        super().draw(surface, mouse_pos)
        
        help_title = self.title_font.render("Справка", True, (200, 200, 255))
        surface.blit(help_title, (50, 50))
        
        if self.current_view == 'keyboard':
            self.draw_controls(surface, self.keyboard_controls, self.content_x)
        else:
            self.draw_controls(surface, self.mouse_controls, self.content_x)
    
    def draw_controls(self, surface, controls, start_x):
        """Отрисовка списка управления"""
        for i, (key, description) in enumerate(controls):
            y_pos = self.start_y + (i * self.line_height)
            
            key_surface = self.small_font.render(key, True, (150, 180, 255))
            surface.blit(key_surface, (start_x, y_pos))
            
            desc_surface = self.small_font.render(description, True, (255, 255, 255))
            surface.blit(desc_surface, (start_x + self.key_column_width, y_pos))