import os
import json
import pygame
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SAVES_DIR = os.path.join(BASE_DIR, 'saves')

class SaveManager:
    def __init__(self):
        self.saves_dir = SAVES_DIR
        os.makedirs(self.saves_dir, exist_ok=True)
        os.makedirs(os.path.join(self.saves_dir, 'screenshots'), exist_ok=True)
    
    def create_save(self, slot, game_state, screenshot=None):
        save_data = {
            'slot': slot,
            'timestamp': datetime.now().isoformat(),
            'game_state': game_state,
            'screenshot_path': None
        }
        
        if screenshot:
            screenshot_path = os.path.join(
                self.saves_dir, 'screenshots', f'save_{slot}.png'
            )
            try:
                pygame.image.save(screenshot, screenshot_path)
                save_data['screenshot_path'] = screenshot_path
            except Exception as e:
                print(f"Ошибка сохранения скриншота: {e}")
        
        save_path = os.path.join(self.saves_dir, f'save_{slot}.json')
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            print(f"Сохранение в слот {slot} создано")
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False
    
    def load_save(self, slot):
        save_path = os.path.join(self.saves_dir, f'save_{slot}.json')
        if not os.path.exists(save_path):
            return None
        
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            print(f"Загружено сохранение из слота {slot}")
            return save_data.get('game_state')
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return None
    
    def get_save_info(self, slot):
        save_path = os.path.join(self.saves_dir, f'save_{slot}.json')
        if not os.path.exists(save_path):
            return None
        
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            return {
                'slot': slot,
                'timestamp': save_data.get('timestamp'),
                'screenshot_path': save_data.get('screenshot_path'),
                'game_state': save_data.get('game_state')
            }
        except:
            return None
    
    def get_all_saves(self):
        saves = []
        for slot in range(1, 10):
            info = self.get_save_info(slot)
            if info:
                saves.append(info)
            else:
                saves.append({'slot': slot, 'timestamp': None, 'screenshot_path': None})
        return saves