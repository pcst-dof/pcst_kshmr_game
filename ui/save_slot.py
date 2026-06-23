import pygame
import os

class SaveSlot:
    def __init__(self, x, y, width, height, slot_number, save_info=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.slot_number = slot_number
        self.save_info = save_info
        self.hovered = False
        
        # Миниатюра
        self.thumbnail = None
        if save_info and save_info.get('screenshot'):
            try:
                self.thumbnail = pygame.image.load(save_info['screenshot'])
                # Необходимый размер миниатюры
                self.thumbnail = pygame.transform.scale(self.thumbnail, (width - 20, height - 80))
            except Exception as e:
                print(f"Error loading thumbnail: {e}")
        
        # Шрифты
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
    
    def draw(self, screen):
        # Цвет рамки (меняется при наведении, прикольно)
        border_color = (150, 150, 150) if self.hovered else (80, 80, 80)
        
        # фон слота
        pygame.draw.rect(screen, (20, 20, 20), self.rect)
        pygame.draw.rect(screen, border_color, self.rect, 3)
        
        # миниатюра или заглушка
        if self.thumbnail:
            thumb_rect = self.thumbnail.get_rect(centerx=self.rect.centerx, top=self.rect.y + 10)
            screen.blit(self.thumbnail, thumb_rect)
        else:
            # заглушка "Empty"
            text = self.font.render(f"Slot {self.slot_number}", True, (100, 100, 100))
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)
        
        # информация (если есть сохранение)
        if self.save_info:
            # Дата
            date_text = self.small_font.render(
                self.save_info.get('date_display', ''), 
                True, (200, 200, 200)
            )
            date_rect = date_text.get_rect(centerx=self.rect.centerx, bottom=self.rect.bottom - 10)
            screen.blit(date_text, date_rect)
            
            # название сцены
            scene_text = self.small_font.render(
                self.save_info.get('scene', ''), 
                True, (150, 150, 150)
            )
            scene_rect = scene_text.get_rect(centerx=self.rect.centerx, bottom=date_rect.top - 5)
            screen.blit(scene_text, scene_rect)
    
    def handle_event(self, event):
        """Обработка событий мыши"""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False