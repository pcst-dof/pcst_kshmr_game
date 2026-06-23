import pygame
from scenes.menu.base_menu import BaseMenu, MY_FONT_PATH, MY_FONT_SIZE


class PauseMenu(BaseMenu):
    """Меню паузы с кнопками"""

    def __init__(self, game, previous_scene=None):
        super().__init__(game, "pause_menu", add_back_button=False)
        self.previous_scene = previous_scene
        self.selected_button = 0
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_width = 260
        button_height = 56
        button_spacing = 20
        start_y = 320

        button_configs = [
            ("Продолжить", self.resume_game),
            ("Настройки", self.open_settings),
            ("Сохранить", self.save_game),
            ("В главное меню", self.to_main_menu),
        ]

        for i, (label, action) in enumerate(button_configs):
            btn_x = (self.game.LOGICAL_W - button_width) // 2
            btn_y = start_y + i * (button_height + button_spacing)

            btn = pygame.sprite.Sprite()
            from ui.button import Button
            btn = Button(
                btn_x, btn_y, button_width, button_height,
                label, (100, 100, 255), (255, 255, 255),
                action=action,
                font_path=MY_FONT_PATH, font_size=MY_FONT_SIZE
            )
            self.buttons.append(btn)

    def resume_game(self):
        if self.previous_scene and self.previous_scene in self.game.scenes:
            self.game.change_scene(self.previous_scene)
        else:
            self.game.change_scene('main_menu')

    def open_settings(self):
        settings = self.game.scenes.get('settings_menu')
        if settings:
            settings.previous_scene = 'pause_menu'
        self.game.change_scene('settings_menu')

    def save_game(self):
        save_menu = self.game.scenes.get('save_menu')
        if save_menu:
            save_menu.previous_scene = 'pause_menu'
        self.game.change_scene('save_menu')

    def to_main_menu(self):
        self.game.change_scene('main_menu')

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_p):
                self.resume_game()
                return True

            if event.key == pygame.K_UP:
                self.selected_button = max(0, self.selected_button - 1)
                return True
            if event.key == pygame.K_DOWN:
                self.selected_button = min(len(self.buttons) - 1, self.selected_button + 1)
                return True
            if event.key == pygame.K_RETURN:
                if self.buttons and 0 <= self.selected_button < len(self.buttons):
                    self.buttons[self.selected_button].action()
                return True

        if action == 'advance':
            if mouse_pos:
                for btn in self.buttons:
                    if btn.rect.collidepoint(mouse_pos):
                        btn.action()
                        return True
            if self.buttons and 0 <= self.selected_button < len(self.buttons):
                self.buttons[self.selected_button].action()
            return True

        if action == 'nav_up':
            self.selected_button = max(0, self.selected_button - 1)
            return True
        if action == 'nav_down':
            self.selected_button = min(len(self.buttons) - 1, self.selected_button + 1)
            return True

        return super().handle_event(event, mouse_pos, action, dt)

    def draw(self, surface, mouse_pos=None):
        super().draw(surface, mouse_pos)

        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        surface.blit(overlay, (0, 0))

        title = self.title_font.render("ПАУЗА", True, (200, 200, 255))
        title_rect = title.get_rect(centerx=self.game.LOGICAL_W // 2, top=180)
        surface.blit(title, title_rect)

        for btn in self.buttons:
            btn.draw(surface, mouse_pos)