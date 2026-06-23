import pygame
from scenes.menu.save_load_menu import SaveLoadMenu


class SaveMenu(SaveLoadMenu):
    def __init__(self, game):
        super().__init__(game, "save_menu", mode='save')
        self.game_state_to_save = ''
        self.screenshot_to_save = None
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_pos:
                # Кнопки страниц
                for i, btn in enumerate(self.page_buttons):
                    if btn.rect.collidepoint(mouse_pos):
                        btn.action()
                        return True
                
                # Кнопка "Вернуться"
                for button in self.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        if button.action:
                            button.action()
                        return True
                
                # Слоты
                start_slot = self.current_page * self.slots_per_page
                end_slot = start_slot + self.slots_per_page
                for slot in self.save_slots[start_slot:end_slot]:
                    rect = slot.get('draw_rect', slot['rect'])
                    if rect.collidepoint(mouse_pos):
                        self.save_to_slot(slot['slot_number'])
                        return True
        
        return False
    
    def save_to_slot(self, slot_number):
        """Сохраняем игру со скриншотом"""
        
        # Сохраняем
        if self.save_manager.create_save(slot_number, self.game_state_to_save, self.screenshot_to_save):
            print(f"✓ Игра сохранена в слот {slot_number}")
            print(f"  Сцена: {self.game_state_to_save}")
            self.load_saves_data() 
    
    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)
        
        title = self.title_font.render(self.title, True, (200, 200, 255))
        screen.blit(title, (self.game.LOGICAL_W // 2 - title.get_width() // 2, 50))
        
        self.load_saves_data()
        self.draw_slots(screen, mouse_pos)
        self.draw_page_buttons(screen, mouse_pos)