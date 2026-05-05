import pygame

class Scene:
    def __init__(self, background_path=None):
        self.background = None
        if background_path:
            try:
                self.background = pygame.image.load(background_path)
                self.background = pygame.transform.scale(self.background, (800, 600))
            except Exception as e:
                print(f"Ошибка загрузки фона {background_path}: {e}")
        self.buttons = []
        self.characters = []  # тут будут персы
        self.text = ""
        self.font = pygame.font.SysFont(None, 24)

    def add_button(self, button):
        self.buttons.append(button)

    def add_character(self, character):
        self.characters.append(character)

    def set_text(self, text):
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event.pos):
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