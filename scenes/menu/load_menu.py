import pygame
from scenes.menu.save_load_menu import SaveLoadMenu


class LoadMenu(SaveLoadMenu):
    def __init__(self, game):
        super().__init__(game, "load_menu", mode='load')
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_pos:
                for i, btn in enumerate(self.page_buttons):
                    if btn.rect.collidepoint(mouse_pos):
                        btn.action()
                        return True
                
                for button in self.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        if button.action:
                            button.action()
                        return True
                
                start_slot = self.current_page * self.slots_per_page
                end_slot = start_slot + self.slots_per_page
                for slot in self.save_slots[start_slot:end_slot]:
                    rect = slot.get('draw_rect', slot['rect'])
                    if rect.collidepoint(mouse_pos):
                        self.load_from_slot(slot['slot_number'])
                        return True
        
        return False
    
    def load_from_slot(self, slot_number):
        """Загружаем игру и переходим к сцене"""
        print(f"Загрузка из слота {slot_number}...")
        
        game_state = self.save_manager.load_save(slot_number)
        
        if not game_state:
            print(f"Ошибка: слот {slot_number} пуст или повреждён")
            return
        
        self.game.load_state(game_state)
        
        scene_name = game_state.get('current_scene', 'main_menu')
        current_dialogue = game_state.get('current_dialogue', 0)
        
        print(f"Состояние загружено")
        print(f"Сцена: {scene_name}")
        
        if scene_name in self.game.scenes:
            self.game.scenes[scene_name].current_dialogue = current_dialogue
            self.game.change_scene(scene_name)
            print(f"Переход к сцене: {scene_name}")
        else:
            print(f"Сцена '{scene_name}' не найдена, загружаем main_menu")
            self.game.change_scene('main_menu')
    
    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)
        
        title = self.title_font.render(self.title, True, (200, 200, 255))
        screen.blit(title, (self.game.LOGICAL_W // 2 - title.get_width() // 2, 50))
        
        self.load_saves_data()
        self.draw_slots(screen, mouse_pos)
        self.draw_page_buttons(screen, mouse_pos)