import os
import pygame
from scenes.scene import Scene
from ui.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40
SMALL_FONT_SIZE = 24
TEXT_FONT_SIZE = 28
LABEL_FONT_SIZE = 24

DEFAULT_BG = 'assets/images/background_0.png'


class HoverButton(Button):
    """Кнопка с активным состоянием (для вкладок и т.п.)"""
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


class BaseMenu(Scene):
    """Базовый класс для всех меню игры"""

    def __init__(self, game, name, background_path=None, add_back_button=True):
        bg = background_path or DEFAULT_BG
        super().__init__(bg, name)
        self.game = game
        self.previous_scene = 'main_menu'

        self.title_font = pygame.font.Font(MY_FONT_PATH, MY_FONT_SIZE)
        self.small_font = pygame.font.Font(MY_FONT_PATH, SMALL_FONT_SIZE)
        self.text_font = pygame.font.Font(MY_FONT_PATH, TEXT_FONT_SIZE)
        self.label_font = pygame.font.Font(MY_FONT_PATH, LABEL_FONT_SIZE)

        if add_back_button:
            self._add_back_button()

    def _add_back_button(self):
        btn_w, btn_h = 260, 56
        btn_x = (self.game.LOGICAL_W - btn_w) // 2
        btn_y = self.game.LOGICAL_H - 130

        back_btn = Button(
            btn_x, btn_y, btn_w, btn_h,
            "Вернуться", (100, 100, 255), (255, 255, 255),
            action=self.go_back,
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE
        )
        self.add_button(back_btn)

    def go_back(self):
        target = self.previous_scene
        self.previous_scene = 'main_menu'
        self.game.change_scene(target)


class Checkbox:
    def __init__(self, x, y, label="", initial_value=False):
        self.x = x
        self.y = y
        self.label = label
        self.checked = initial_value
        self.rect = pygame.Rect(x, y, 20, 20)
        self.hovered = False

        try:
            self.font = pygame.font.Font(MY_FONT_PATH, LABEL_FONT_SIZE)
        except:
            self.font = pygame.font.SysFont(None, LABEL_FONT_SIZE)

    def handle_event(self, event, mouse_pos):
        if mouse_pos is None:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_pos):
                self.checked = not self.checked
                return True

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(mouse_pos)

        return False

    def draw(self, screen, mouse_pos=None):
        color = (100, 100, 180) if self.hovered else (70, 70, 130)
        pygame.draw.rect(screen, color, self.rect, border_radius=3)
        pygame.draw.rect(screen, (140, 140, 220), self.rect, width=2, border_radius=3)

        if self.checked:
            pygame.draw.line(screen, (255, 255, 255),
                           (self.x + 4, self.y + 10),
                           (self.x + 9, self.y + 16), 2)
            pygame.draw.line(screen, (255, 255, 255),
                           (self.x + 9, self.y + 16),
                           (self.x + 17, self.y + 4), 2)

        label_surface = self.font.render(self.label, True, (220, 220, 220))
        screen.blit(label_surface, (self.x + 30, self.y + 2))