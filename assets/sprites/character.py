import pygame

class Character:
    def __init__(self, image_path, x, y):
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
        except pygame.error as e:
            print(f"ошибка персонажа {image_path}: {e}")
            self.image = None
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 100, 150) if self.image else None

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))