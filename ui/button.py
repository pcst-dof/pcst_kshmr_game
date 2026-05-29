import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, text_color, action=None, font_path=None, font_size=36):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.accent_color = color
        self.text_color = text_color
        self.hover_text_color = (255, 255, 255)
        self.shadow_color = (0, 0, 0)
        self.hover_outline = color
        self.base_outline = (255, 255, 255)
        self.outline_width = 2
        self.action = action

        if font_path:
            try:
                self.font = pygame.font.Font(font_path, font_size)
            except FileNotFoundError:
                print(f"шрифт {font_path} не найден! использую стандартный.")
                self.font = pygame.font.SysFont(None, font_size)
        else:
            self.font = pygame.font.SysFont(None, font_size)

    def draw(self, screen, mouse_pos):
        hovered = mouse_pos is not None and self.rect.collidepoint(mouse_pos)

        text_color = self.hover_text_color if hovered else self.text_color
        text_surface = self.font.render(self.text, True, text_color)
        shadow_surface = self.font.render(self.text, True, self.shadow_color)
        shadow_surface.set_alpha(200)

        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - text_surface.get_height()) // 2

        text_rect = pygame.Rect(text_x, text_y, text_surface.get_width(), text_surface.get_height())
        screen.blit(shadow_surface, text_rect.move(3, 3))
        screen.blit(text_surface, text_rect)

        outline_color = self.hover_outline if hovered else self.base_outline
        pygame.draw.rect(screen, outline_color, self.rect, self.outline_width, border_radius=12)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)