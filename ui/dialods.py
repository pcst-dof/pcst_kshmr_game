import pygame

class ConfirmationDialog:
    """
    Модальное окно с вопросом "Вы уверены?"
    """
    def __init__(self, screen, message, on_confirm, on_cancel=None):
        self.screen = screen
        self.message = message
        self.on_confirm = on_confirm 
        self.on_cancel = on_cancel
        self.active = True
        
        # размеры окна
        self.width = 600
        self.height = 250
        self.x = (screen.get_width() - self.width) // 2
        self.y = (screen.get_height() - self.height) // 2
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # кнопки Yes/No
        btn_width = 120
        btn_height = 50
        btn_y = self.y + self.height - 80
        
        self.yes_btn = pygame.Rect(self.x + 100, btn_y, btn_width, btn_height)
        self.no_btn = pygame.Rect(self.x + self.width - 220, btn_y, btn_width, btn_height)
        
        self.font = pygame.font.Font(None, 28)
        self.btn_font = pygame.font.Font(None, 24)
        
        self.hovered_yes = False
        self.hovered_no = False
    
    def draw(self):
        # фон, затемнение
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        
        # окно диалога
        pygame.draw.rect(self.screen, (10, 10, 10), self.rect)
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect, 3)
        
        # текст сообщения
        lines = self.message.split('\n')
        y_offset = self.y + 40
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(centerx=self.rect.centerx, top=y_offset)
            self.screen.blit(text_surface, text_rect)
            y_offset += 40
        
        # кнопочки цветастые
        yes_color = (100, 200, 100) if self.hovered_yes else (50, 100, 50)
        no_color = (200, 100, 100) if self.hovered_no else (100, 50, 50)
        
        pygame.draw.rect(self.screen, yes_color, self.yes_btn)
        pygame.draw.rect(self.screen, no_color, self.no_btn)
        
        yes_text = self.btn_font.render("Yes", True, (255, 255, 255))
        no_text = self.btn_font.render("No", True, (255, 255, 255))
        
        self.screen.blit(yes_text, yes_text.get_rect(center=self.yes_btn.center))
        self.screen.blit(no_text, no_text.get_rect(center=self.no_btn.center))
    
    def handle_event(self, event):
        if not self.active:
            return False
        
        if event.type == pygame.MOUSEMOTION:
            self.hovered_yes = self.yes_btn.collidepoint(event.pos)
            self.hovered_no = self.no_btn.collidepoint(event.pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.yes_btn.collidepoint(event.pos):
                self.active = False
                if self.on_confirm:
                    self.on_confirm()
                return True
            elif self.no_btn.collidepoint(event.pos):
                self.active = False
                if self.on_cancel:
                    self.on_cancel()
                return True
        
        return False