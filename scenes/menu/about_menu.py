import pygame
from scenes.menu.base_menu import BaseMenu


class AboutMenu(BaseMenu):
    def __init__(self, game):
        super().__init__(game, "about_menu")
        self.set_text("О игре")

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