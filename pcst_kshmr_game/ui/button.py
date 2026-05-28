import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, text_color, action=None, hover_color=None, font_size=28):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.action = action
        self.hover_color = hover_color or tuple(min(255, c + 40) for c in color)
        self.font = pygame.font.SysFont(None, font_size)
        self.hovered = False

    def set_hover(self, hovered):
        self.hovered = hovered

    def draw(self, screen):
        text_color = self.hover_color if self.hovered else self.text_color
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        shadow_surface = self.font.render(self.text, True, (0, 0, 0))
        shadow_rect = shadow_surface.get_rect(center=(self.rect.centerx + 2, self.rect.centery + 2))
        screen.blit(shadow_surface, shadow_rect)
        screen.blit(text_surface, text_rect)

        if self.hovered:
            line_y = text_rect.bottom + 5
            pygame.draw.line(screen, self.hover_color, (text_rect.left, line_y), (text_rect.right, line_y), 2)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    