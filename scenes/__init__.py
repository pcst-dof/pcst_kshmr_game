import pygame
from scenes.scene import Scene
from ui.button import Button
from scenes.menu.main_menu import MainMenu
from scenes.menu.settings_menu import SettingsMenu
from scenes.menu.load_menu import LoadMenu
from scenes.menu.help_menu import HelpMenu
from scenes.menu.about_menu import AboutMenu
from scenes.menu.save_menu import SaveMenu
from scenes.locations import Place_0, Place_1, Place_2

class StartScene(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.jpg')
        self.game = game
        self.set_text("What's your name?")

        # Input state
        self.input_text = ""
        self.input_active = True
        self.box_w, self.box_h = 500, 60
        self.box_x = (self.game.LOGICAL_W - self.box_w) // 2
        self.box_y = 340
        self.box_rect = pygame.Rect(self.box_x, self.box_y, self.box_w, self.box_h)
        self.cursor_visible = True
        self.last_cursor_toggle = pygame.time.get_ticks()

        # кнопка далее (по центру)
        btn_w, btn_h = 220, 70
        btn_x = (self.game.LOGICAL_W - btn_w) // 2
        btn_y = 420
        next_button = Button(btn_x, btn_y, btn_w, btn_h, "Next >", (180, 180, 180), (200, 200, 200), self.go_to_scene1, font_size=48)
        self.add_button(next_button)

    def draw(self, screen, mouse_pos=None):
        # рисуем фон и затемнение через базовый draw
        super().draw(screen, mouse_pos)

        # Вопрос в центре
        title_font = pygame.font.SysFont(None, 36)
        question_surf = title_font.render("What's your name?", True, (230, 230, 230))
        qx = (self.game.LOGICAL_W - question_surf.get_width()) // 2
        qy = 300
        screen.blit(question_surf, (qx, qy))

        # Рисуем видимое поле ввода
        pygame.draw.rect(screen, (20, 20, 20), self.box_rect)
        pygame.draw.rect(screen, (180, 180, 180), self.box_rect, 2, border_radius=8)

        display_text = self.input_text if self.input_text else "Enter your name..."
        txt_surf = self.font.render(display_text, True, (200, 200, 200))
        screen.blit(txt_surf, (self.box_x + 16, self.box_y + (self.box_h - txt_surf.get_height()) // 2))

        # Мигание курсора
        now = pygame.time.get_ticks()
        if now - self.last_cursor_toggle > 500:
            self.cursor_visible = not self.cursor_visible
            self.last_cursor_toggle = now

        if self.input_active and self.cursor_visible:
            cursor_x = self.box_x + 16 + txt_surf.get_width() + 2
            cursor_y = self.box_y + 12
            pygame.draw.rect(screen, (220, 220, 220), (cursor_x, cursor_y, 2, self.box_h - 24))

        # Нижняя панель с опциями (стилизованная, полупрозрачная)
        footer_y = self.game.LOGICAL_H - 40
        menu_font = pygame.font.SysFont(None, 20)
        menu_items = ["Back", "History", "Skip", "Auto", "Save", "Q.Save", "Q.Load", "Prefs"]
        spacing = 80
        start_x = (self.game.LOGICAL_W - spacing * len(menu_items)) // 2
        for i, item in enumerate(menu_items):
            item_surf = menu_font.render(item, True, (140, 140, 140))
            ix = start_x + i * spacing
            screen.blit(item_surf, (ix, footer_y))

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        # Обрабатываем клики по полю ввода для фокуса
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None and self.box_rect.collidepoint(click_pos):
                self.input_active = True
                return True
            # если клик вне поля — снимаем фокус
            if click_pos is not None and not self.box_rect.collidepoint(click_pos):
                # но не сбрасываем фокус если клик по кнопке Next (пусть кнопка обработает)
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True

        # Обрабатываем текстовый ввод, только когда поле активно
        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
                return True
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                # подтвердить и идти далее
                self.go_to_scene1()
                return True
            else:
                char = event.unicode
                if char.isprintable() and len(self.input_text) < 30:
                    self.input_text += char
                    return True

        # делегируем остальным обработчикам (например, кнопкам и навигации)
        return super().handle_event(event, mouse_pos=mouse_pos, action=action, dt=dt)

    def go_to_scene1(self):
        # Сохраняем введённое имя в объекте игры
        name = self.input_text.strip() or "Player"
        self.game.player_name = name
        # После ввода имени переходим к начальной локации игры
        self.game.change_scene("0")

class Scene1(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_1.jpg')
        self.game = game
        self.set_text("тут уже текст по сцене")
        look_button = Button(200, 500, 100, 50, "выбор 1", (255, 0, 0), (0, 0, 0), self.look_around)
        exit_button = Button(500, 500, 100, 50, "выбор 2", (0, 0, 255), (255, 255, 255), self.exit_room)
        self.add_button(look_button)
        self.add_button(exit_button)

    def look_around(self):
        print("выбрано: выбор 1")
        # логика перехода

    def exit_room(self):
        print("выбрано: выбор 2")
        # логика перехода