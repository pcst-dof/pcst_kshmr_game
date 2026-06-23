import pygame

class Slider:
    def __init__(self, x, y, width, height, min_value=0, max_value=100, 
                 initial_value=50, label=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.label = label
        
        self.rect = pygame.Rect(x, y, width, height)
        
        # Позиция ползунка
        self.handle_width = 10
        self.handle_rect = self._calculate_handle_rect()
        
        # Состояние
        self.dragging = False
        self.hovered = False
        
        # Шрифт для подписи
        try:
            self.font = pygame.font.Font(None, 24)
        except:
            self.font = pygame.font.SysFont(None, 24)
    
    def _calculate_handle_rect(self):
        """Позиция ползунка на основе значения"""
        ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        handle_x = self.x + int(ratio * (self.width - self.handle_width))
        handle_y = self.y - 3
        return pygame.Rect(handle_x, handle_y, self.handle_width, self.height + 6)
    
    def get_value_from_pos(self, x):
        """Значение позиции мыши"""
        ratio = (x - self.x) / self.width
        ratio = max(0, min(1, ratio))
        return int(self.min_value + ratio * (self.max_value - self.min_value))
    
    def handle_event(self, event, mouse_pos):
        """Обработка событий"""
        if mouse_pos is None:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.handle_rect.collidepoint(mouse_pos):
                self.dragging = True
                return True
            elif self.rect.collidepoint(mouse_pos):
                self.value = self.get_value_from_pos(mouse_pos[0])
                self.handle_rect = self._calculate_handle_rect()
                return True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.value = self.get_value_from_pos(mouse_pos[0])
                self.handle_rect = self._calculate_handle_rect()
                return True
            
            self.hovered = self.rect.collidepoint(mouse_pos)
        
        return False
    
    def draw(self, screen):
        if self.label:
            label_surface = self.font.render(self.label, True, (220, 220, 220))
            screen.blit(label_surface, (self.x, self.y - 25))
        
        # Тёмно-фиолетовый фон
        track_color = (70, 70, 130) if not self.hovered else (80, 80, 140)
        pygame.draw.rect(screen, track_color, self.rect, border_radius=3)
        
        # Светло-фиолетовая заполненная часть
        fill_width = int((self.value - self.min_value) / (self.max_value - self.min_value) * self.width)
        fill_rect = pygame.Rect(self.x, self.y, fill_width, self.height)
        pygame.draw.rect(screen, (100, 100, 255), fill_rect, border_radius=3)
        
        # Яркий фиолетовый ползунок
        handle_color = (120, 120, 255) if self.dragging else (100, 100, 200)
        pygame.draw.rect(screen, handle_color, self.handle_rect, border_radius=5)
        pygame.draw.rect(screen, (150, 150, 255), self.handle_rect, width=1, border_radius=5)
        
        # Значение
        value_text = self.font.render(str(self.value), True, (255, 255, 255))
        value_rect = value_text.get_rect(center=(self.x + self.width // 2, self.y + self.height + 20))
        screen.blit(value_text, value_rect)