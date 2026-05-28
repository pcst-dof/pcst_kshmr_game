import pygame
from pathlib import Path

class Scene:
    def __init__(self, game=None, background_path=None):
        self.game = game
        self.background = None
        if background_path:
            try:
                background_file = self._get_resource_path(background_path)
                self.background = pygame.image.load(background_file)
                self.background = pygame.transform.scale(self.background, (800, 600))
            except Exception as e:
                print(f"Ошибка загрузки фона {background_path}: {e}")
        self.buttons = []
        self.characters = []  # тут будут персы
        self.text = ""
        self.font = pygame.font.SysFont(None, 24)

    def _translate_mouse(self, pos):
        if not self.game:
            return pos
        win_w, win_h = self.game.screen.get_size()
        scale = min(win_w / self.game.LOGICAL_W, win_h / self.game.LOGICAL_H)
        new_w = int(self.game.LOGICAL_W * scale)
        new_h = int(self.game.LOGICAL_H * scale)
        offset_x = (win_w - new_w) // 2
        offset_y = (win_h - new_h) // 2

        x, y = pos
        x -= offset_x
        y -= offset_y

        if x < 0 or y < 0 or x > new_w or y > new_h:
            return -1, -1

        logical_x = int(x / scale)
        logical_y = int(y / scale)
        return logical_x, logical_y

    def add_button(self, button):
        self.buttons.append(button)

    def _get_resource_path(self, relative_path):
        base_dir = Path(__file__).resolve().parent.parent
        return str(base_dir / relative_path)

    def add_character(self, character):
        self.characters.append(character)

    def set_text(self, text):
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            pos = self._translate_mouse(event.pos)
            for button in self.buttons:
                button.set_hover(button.is_clicked(pos))
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = self._translate_mouse(event.pos)
            for button in self.buttons:
                if button.is_clicked(pos):
                    if button.action:
                        button.action()
                    return True
        return False

    def draw(self, screen):
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill((0, 0, 255))

        # и тут будут персы
        for character in self.characters:
            character.draw(screen)

        if self.text:
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            screen.blit(text_surface, (50, 50))

        for button in self.buttons:
            button.draw(screen)