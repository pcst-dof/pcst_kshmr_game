import os
import pygame

from scenes.menu.main_menu import BASE_DIR
from scenes.scene import Scene
from ui.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40


class AboutMenu(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.png')
        self.game = game
        self.set_text("О игре")

        try:
            self.text_font = pygame.font.Font(MY_FONT_PATH, 28)
            self.title_font = pygame.font.Font(MY_FONT_PATH, 32)
        except FileNotFoundError:
            self.text_font = pygame.font.SysFont(None, 28)
            self.title_font = pygame.font.SysFont(None, 32)

        self.about_lines = [
            "KNOW WHO YOU ARE",
            "",
            "Психологический хоррор",
            "о потере себя и поиске истины.",
            "",
            "• Исследуй мрачные локации",
            "• Раскрывай тайны прошлого",
            "• Принимай решения, что меняют всё",
            "",
            "Версия 1.0",
            "Автор хочет спать, но не может.",
            "",
            "2026"
        ]

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
            lambda: game.change_scene("main_menu"),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE
        )
        self.add_button(back_btn)

    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)

        y_offset = 140
        line_height = 38

        for i, line in enumerate(self.about_lines):
            if line == "":
                y_offset += 25
                continue

            if i == 0:
                font = self.title_font
                color = (255, 255, 255)
            else:
                font = self.text_font
                color = (220, 220, 220)

            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(self.game.LOGICAL_W // 2, y_offset))
            screen.blit(text_surface, text_rect)

            y_offset += line_height

