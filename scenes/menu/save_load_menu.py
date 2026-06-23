import os
import pygame
from datetime import datetime
from scenes.menu.base_menu import BaseMenu, MY_FONT_PATH, MY_FONT_SIZE
from utils.save_manager import SaveManager


class SaveLoadMenu(BaseMenu):
    """Базовый класс для SaveMenu и LoadMenu"""
    
    def __init__(self, game, name, mode='save'):
        super().__init__(game, name)
        self.mode = mode
        self.save_manager = SaveManager()
        
        self.date_font = pygame.font.Font(None, 22)
        self.title = "LOAD GAME" if mode == 'load' else "SAVE GAME"
        
        # Размеры и позиции
        self.slot_width = 320
        self.slot_height = 170
        self.slot_spacing_x = 30
        self.slot_spacing_y = 25
        self.start_x = 120
        self.start_y = 135
        self.cols = 3
        self.rows = 3
        self.slots_per_page = self.cols * self.rows
        
        self.total_slots = 27
        self.total_pages = 3
        
        self.save_slots = []
        self.create_slots()
        
        self.current_page = 0
        self.page_buttons = []
        self.create_page_buttons()
    
    def create_slots(self):
        for i in range(self.total_slots):
            row = i // self.cols
            col = i % self.cols
            
            x = self.start_x + col * (self.slot_width + self.slot_spacing_x)
            y = self.start_y + row * (self.slot_height + self.slot_spacing_y)
            
            slot_rect = pygame.Rect(x, y, self.slot_width, self.slot_height)
            
            self.save_slots.append({
                'slot_number': i + 1,
                'rect': slot_rect,
                'screenshot': None,
                'timestamp': None,
            })
    
    def create_page_buttons(self):
        from ui.button import Button
        
        button_width = 50
        spacing = 20
        total_width = self.total_pages * button_width + (self.total_pages - 1) * spacing
        start_x = (self.game.LOGICAL_W - total_width) // 2
        
        for i in range(self.total_pages):
            btn = Button(
                start_x + i * (button_width + spacing),
                self.game.LOGICAL_H - 180,
                button_width, 40,
                str(i + 1), (70, 70, 130), (255, 255, 255),
                lambda page=i: self.go_to_page(page),
                font_path=MY_FONT_PATH, font_size=24
            )
            self.page_buttons.append(btn)
    
    def go_to_page(self, page):
        if 0 <= page < self.total_pages:
            self.current_page = page
    
    def load_saves_data(self):
        all_saves = self.save_manager.get_all_saves()
        
        for save_info in all_saves:
            slot_idx = save_info['slot'] - 1
            if slot_idx < len(self.save_slots):
                slot = self.save_slots[slot_idx]
                slot['timestamp'] = save_info.get('timestamp')
                
                screenshot_path = save_info.get('screenshot_path')
                if screenshot_path and os.path.exists(screenshot_path):
                    try:
                        img = pygame.image.load(screenshot_path).convert_alpha()
                        target_w = self.slot_width - 20
                        target_h = self.slot_height - 70
                        slot['screenshot'] = pygame.transform.smoothscale(img, (target_w, target_h))
                    except:
                        slot['screenshot'] = None
    
    def format_timestamp(self, timestamp_str):
        if not timestamp_str:
            return "Empty Slot"
        try:
            dt = datetime.fromisoformat(timestamp_str)
            return dt.strftime("%d.%m.%Y  %H:%M")
        except:
            return timestamp_str
    
    def draw_slots(self, screen, mouse_pos=None):
        start_slot = self.current_page * self.slots_per_page
        end_slot = start_slot + self.slots_per_page
        
        for local_index, slot in enumerate(self.save_slots[start_slot:end_slot]):
            row = local_index // self.cols
            col = local_index % self.cols
            
            x = self.start_x + col * (self.slot_width + self.slot_spacing_x)
            y = self.start_y + row * (self.slot_height + self.slot_spacing_y)
            
            slot['draw_rect'] = pygame.Rect(x, y, self.slot_width, self.slot_height)
            self.draw_slot(screen, slot, mouse_pos)
    
    def draw_slot(self, screen, slot, mouse_pos):
        rect = slot.get('draw_rect', slot['rect'])
        hovered = mouse_pos and rect.collidepoint(mouse_pos)
        
        bg_color = (60, 60, 90) if hovered else (40, 40, 60)
        pygame.draw.rect(screen, bg_color, rect, border_radius=8)
        
        border_color = (150, 150, 220) if hovered else (100, 100, 150)
        pygame.draw.rect(screen, border_color, rect, width=2, border_radius=8)
        
        slot_num_surface = self.small_font.render(f"Slot {slot['slot_number']}", True, (180, 180, 230))
        screen.blit(slot_num_surface, (rect.x + 10, rect.y + 8))
        
        if slot['screenshot']:
            screenshot_rect = slot['screenshot'].get_rect(x=rect.x + 10, y=rect.y + 35)
            screen.blit(slot['screenshot'], screenshot_rect)
        else:
            empty_text = self.small_font.render("Empty", True, (100, 100, 120))
            empty_rect = empty_text.get_rect(center=rect.center)
            screen.blit(empty_text, (empty_rect.x, empty_rect.y - 20))
        
        date_text = self.format_timestamp(slot['timestamp'])
        date_surface = self.date_font.render(date_text, True, (180, 180, 220))
        date_rect = date_surface.get_rect(centerx=rect.centerx, bottom=rect.bottom - 10)
        screen.blit(date_surface, date_rect)
    
    def draw_page_buttons(self, screen, mouse_pos=None):
        for i, btn in enumerate(self.page_buttons):
            btn.accent_color = (120, 120, 200) if i == self.current_page else (70, 70, 130)
            btn.draw(screen, mouse_pos)