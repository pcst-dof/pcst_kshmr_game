import pygame

class InputManager:
    """Обработка ввода и возвращение игровых действий"""
    
    def __init__(self):
        self.skip_held = False
        self.skip_toggled = False
        self.ui_hidden = False
    
    def process(self, event, mouse_click=None):
        """
        Обработка события и возврат строки-действия.
        Пример: 'advance', 'menu', 'skip_hold' или None
        """
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                return 'advance'
            if event.key == pygame.K_UP: return 'nav_up'
            if event.key == pygame.K_DOWN: return 'nav_down'
            if event.key == pygame.K_LEFT: return 'nav_left'
            if event.key == pygame.K_RIGHT: return 'nav_right'
            if event.key == pygame.K_ESCAPE: return 'menu'
            if event.key in (pygame.K_LCTRL, pygame.K_RCTRL):
                self.skip_held = True
                return 'skip_hold'
            if event.key == pygame.K_TAB:
                self.skip_toggled = not self.skip_toggled
                return 'skip_toggle'
            if event.key == pygame.K_PAGEUP: return 'dialogue_back'
            if event.key == pygame.K_PAGEDOWN: return 'dialogue_forward'
            if event.key == pygame.K_h:
                self.ui_hidden = not self.ui_hidden
                return 'toggle_ui'
            if event.key == pygame.K_s: return 'screenshot'
            if event.key == pygame.K_v: return 'toggle_voice'
            if event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                return 'accessibility'
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LCTRL, pygame.K_RCTRL):
                self.skip_held = False
                return 'skip_release'
        
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_click:
            if event.button == 1: return 'advance'  
            if event.button == 2:             
                self.ui_hidden = not self.ui_hidden
                return 'toggle_ui'
            if event.button == 3: return 'menu'    
            if event.button == 4: return 'dialogue_back'  
            if event.button == 5: return 'dialogue_forward' 
        
        return None
    
    def is_skipping(self):
        return self.skip_held or self.skip_toggled
    
    def is_ui_hidden(self):
        return self.ui_hidden