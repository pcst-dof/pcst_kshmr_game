import os
import pygame

from scenes.scene import Scene
from ui.button import Button
from ui.actions.actions import (
    start_game,
    load_game,
    open_options,
    open_help,
    open_about,
    exit_game,
)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__('assets/images/main_menu.jpg')
        self.game = game
        self.title = "know who you are"
        self.title_color = (245, 245, 245)
        self.title_shadow = (0, 0, 0)
        self.title_font = self._load_title_font()
        self.set_text("")
        
        # расстановка кнопок по центру
        button_width = 300
        button_height = 50
        button_spacing = 70
        button_x = (self.game.LOGICAL_W - button_width) // 2
        button_y_start = 420
        
        start_btn = Button(
            button_x, 
            button_y_start, 
            button_width, 
            button_height, 
            "start", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: start_game(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        load_btn = Button(
            button_x, 
            button_y_start + button_spacing, 
            button_width, 
            button_height, 
            "load", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: load_game(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        options_btn = Button(
            button_x, 
            button_y_start + button_spacing * 2, 
            button_width, 
            button_height, 
            "options", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: open_options(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        help_btn = Button(
            button_x, 
            button_y_start + button_spacing * 3, 
            button_width, 
            button_height, 
            "help", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: open_help(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        about_btn = Button(
            button_x, 
            button_y_start + button_spacing * 4, 
            button_width, 
            button_height, 
            "about", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: open_about(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        exit_btn = Button(
            button_x, 
            button_y_start + button_spacing * 5, 
            button_width, 
            button_height, 
            "exit", 
            (180, 180, 180), 
            (180, 180, 180), 
            lambda: exit_game(game),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        
        self.add_button(start_btn)
        self.add_button(load_btn)
        self.add_button(options_btn)
        self.add_button(help_btn)
        self.add_button(about_btn)
        self.add_button(exit_btn)

    def _load_title_font(self):
        try:
            return pygame.font.Font(MY_FONT_PATH, 72)
        except FileNotFoundError:
            print(f"шрифт {MY_FONT_PATH} не найден! использую системный.")
            return pygame.font.SysFont(None, 72)

    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)

        title_surface = self.title_font.render(self.title, True, self.title_color)
        title_shadow = self.title_font.render(self.title, True, self.title_shadow)
        title_shadow.set_alpha(220)

        title_rect = title_surface.get_rect(midtop=(screen.get_width() // 2, 300))
        screen.blit(title_shadow, title_rect.move(4, 4))
        screen.blit(title_surface, title_rect)
