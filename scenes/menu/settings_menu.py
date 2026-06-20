import game
import pygame
import json
import os
from scenes.menu.main_menu import MY_FONT_SIZE
from scenes.scene import Scene
from ui.slider import Slider
from ui.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')

class SettingsMenu(Scene):
    def __init__(self, game):
        super().__init__(background_path='assets/images/background_0.png')
        self.game = game
        self.settings = self.load_settings()
        self.sliders = {}
        self.checkboxes = {}
        
        try:
            self.title_font = pygame.font.Font(MY_FONT_PATH, 40)
            self.label_font = pygame.font.Font(MY_FONT_PATH, 24)
        except:
            self.title_font = pygame.font.SysFont(None, 40)
            self.label_font = pygame.font.SysFont(None, 24)
        
        # Кнопка "Вернуться" — точно как в HelpMenu
        back_button_width = 260
        back_button_height = 56
        back_button_x = (self.game.LOGICAL_W - back_button_width) // 2
        back_button_y = self.game.LOGICAL_H - 130

        back_btn = Button(
            back_button_x, back_button_y, back_button_width, back_button_height,
            "Вернуться", (100, 100, 255), (255, 255, 255),
            lambda: self.save_and_exit(),
            font_path=MY_FONT_PATH, font_size=MY_FONT_SIZE 
        )
        self.add_button(back_btn)
        
        self.create_sliders()
        self.create_checkboxes()
    
    def save_and_exit(self):
        """Сохраняет настройки и возвращается в главное меню"""
        self.save_settings()
        self.game.change_scene("main_menu")
    
    def create_sliders(self):
        slider_y_start = 220
        slider_spacing = 70
        
        self.sliders['music_volume'] = Slider(
            x=450, y=slider_y_start, width=300, height=8,
            min_value=0, max_value=100,
            initial_value=self.settings.get('music_volume', 70),
            label="Music Volume"
        )
        
        self.sliders['sound_volume'] = Slider(
            x=450, y=slider_y_start + slider_spacing, width=300, height=8,
            min_value=0, max_value=100,
            initial_value=self.settings.get('sound_volume', 70),
            label="Sound Volume"
        )
        
        self.sliders['voice_volume'] = Slider(
            x=450, y=slider_y_start + slider_spacing * 2, width=300, height=8,
            min_value=0, max_value=100,
            initial_value=self.settings.get('voice_volume', 70),
            label="Voice Volume"
        )
        
        self.sliders['text_speed'] = Slider(
            x=450, y=slider_y_start + slider_spacing * 3, width=300, height=8,
            min_value=1, max_value=10,
            initial_value=self.settings.get('text_speed', 5),
            label="Text Speed"
        )
        
        self.sliders['auto_forward'] = Slider(
            x=450, y=slider_y_start + slider_spacing * 4, width=300, height=8,
            min_value=1, max_value=10,
            initial_value=self.settings.get('auto_forward', 5),
            label="Auto-Forward Time"
        )
    
    def create_checkboxes(self):
        checkbox_y_start = 220
        checkbox_spacing = 40
        
        # Левая колонка — Display
        self.checkboxes['fullscreen'] = Checkbox(
            x=150, y=checkbox_y_start,
            label="Fullscreen",
            initial_value=self.settings.get('fullscreen', False)
        )
        
        self.checkboxes['window'] = Checkbox(
            x=150, y=checkbox_y_start + checkbox_spacing,
            label="Window",
            initial_value=not self.settings.get('fullscreen', False)
        )
        
        # Правая колонка — Skip (x=900)
        self.checkboxes['skip_unseen'] = Checkbox(
            x=900, y=checkbox_y_start,
            label="Unseen Text",
            initial_value=self.settings.get('skip_unseen', False)
        )
        
        self.checkboxes['skip_after_choices'] = Checkbox(
            x=900, y=checkbox_y_start + checkbox_spacing,
            label="After Choices",
            initial_value=self.settings.get('skip_after_choices', False)
        )
        
        self.checkboxes['skip_transitions'] = Checkbox(
            x=900, y=checkbox_y_start + checkbox_spacing * 2,
            label="Transitions",
            initial_value=self.settings.get('skip_transitions', False)
        )
        
        # Mute All под правой колонкой
        self.checkboxes['mute_all'] = Checkbox(
            x=900, y=checkbox_y_start + checkbox_spacing * 4,
            label="Mute All",
            initial_value=self.settings.get('mute_all', False)
        )
    
    def load_settings(self):
        settings_path = os.path.join(BASE_DIR, 'saves', 'settings.json')
        if os.path.exists(settings_path):
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            'music_volume': 70,
            'sound_volume': 70,
            'voice_volume': 70,
            'text_speed': 5,
            'auto_forward': 5,
            'fullscreen': False,
            'skip_unseen': False,
            'skip_after_choices': False,
            'skip_transitions': False,
            'mute_all': False,
            'language': 'english'
        }
    
    def save_settings(self):
        settings_path = os.path.join(BASE_DIR, 'saves', 'settings.json')
        os.makedirs(os.path.dirname(settings_path), exist_ok=True)
        
        settings = {
            'music_volume': self.sliders['music_volume'].value,
            'sound_volume': self.sliders['sound_volume'].value,
            'voice_volume': self.sliders['voice_volume'].value,
            'text_speed': self.sliders['text_speed'].value,
            'auto_forward': self.sliders['auto_forward'].value,
            'fullscreen': self.checkboxes['fullscreen'].checked,
            'skip_unseen': self.checkboxes['skip_unseen'].checked,
            'skip_after_choices': self.checkboxes['skip_after_choices'].checked,
            'skip_transitions': self.checkboxes['skip_transitions'].checked,
            'mute_all': self.checkboxes['mute_all'].checked,
            'language': 'english'
        }
        
        try:
            with open(settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=2)
            print("✓ Настройки сохранены")
        except Exception as e:
            print(f"✗ Ошибка сохранения настроек: {e}")
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        # Обработка ползунков
        for slider in self.sliders.values():
            if slider.handle_event(event, mouse_pos):
                self.apply_settings()  # ← ДОБАВЛЕНО!
                return True
        
        # Обработка чекбоксов
        for checkbox in self.checkboxes.values():
            if checkbox.handle_event(event, mouse_pos):
                # Логика связи fullscreen/window
                if checkbox is self.checkboxes['fullscreen'] and checkbox.checked:
                    self.checkboxes['window'].checked = False
                elif checkbox is self.checkboxes['window'] and checkbox.checked:
                    self.checkboxes['fullscreen'].checked = False
                
                self.apply_settings()  # ← ДОБАВЛЕНО!
                return True
        
        # Escape для выхода
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.save_and_exit()
            return True
        
        # Базовый класс обработает клики по кнопкам (включая "Вернуться")
        return super().handle_event(event, mouse_pos, action, dt)
    
    def apply_settings(self):
        """Применяет текущие настройки к игре"""
        if not self.game:
            return
        
        # Громкость музыки
        if hasattr(self.game, 'music_volume'):
            self.game.music_volume = self.sliders['music_volume'].value / 100.0
        
        # Fullscreen
        want_fullscreen = self.checkboxes['fullscreen'].checked
        current_fullscreen = getattr(self.game, 'fullscreen', False)
        
        if want_fullscreen != current_fullscreen:
            print(f"Переключаю fullscreen: {current_fullscreen} → {want_fullscreen}")
            try:
                self.game.toggle_fullscreen()
                self.settings['fullscreen'] = want_fullscreen
            except Exception as e:
                print(f"✗ Ошибка переключения fullscreen: {e}")
                # Возвращаем чекбокс в исходное состояние
                self.checkboxes['fullscreen'].checked = current_fullscreen
                self.checkboxes['window'].checked = not current_fullscreen
    
    def update(self, dt):
        pass
    
    def draw(self, screen, mouse_pos=None):
        # Фон
        super().draw(screen, mouse_pos)
        
        # Заголовок СЛЕВА СВЕРХУ
        title = self.title_font.render("SETTINGS", True, (200, 200, 255))
        screen.blit(title, (50, 50))
        
        # Заголовки колонок
        display_label = self.label_font.render("Display", True, (200, 200, 200))
        screen.blit(display_label, (150, 170))
        
        audio_label = self.label_font.render("Audio", True, (200, 200, 200))
        screen.blit(audio_label, (450, 170))
        
        skip_label = self.label_font.render("Skip", True, (200, 200, 200))
        screen.blit(skip_label, (900, 170))
        
        # Рисуем чекбоксы
        for checkbox in self.checkboxes.values():
            checkbox.draw(screen, mouse_pos)
        
        # Рисуем ползунки
        for slider in self.sliders.values():
            slider.draw(screen)
        
        # Кнопки рисуются через базовый класс
        for button in self.buttons:
            button.draw(screen, mouse_pos)


class Checkbox:
    def __init__(self, x, y, label="", initial_value=False):
        self.x = x
        self.y = y
        self.label = label
        self.checked = initial_value
        self.rect = pygame.Rect(x, y, 20, 20)
        self.hovered = False
        
        try:
            self.font = pygame.font.Font(MY_FONT_PATH, 24)
        except:
            self.font = pygame.font.SysFont(None, 24)
    
    def handle_event(self, event, mouse_pos):
        if mouse_pos is None:
            return False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_pos):
                self.checked = not self.checked
                return True
        
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(mouse_pos)
        
        return False
    
    def draw(self, screen, mouse_pos=None):
        color = (100, 100, 180) if self.hovered else (70, 70, 130)
        pygame.draw.rect(screen, color, self.rect, border_radius=3)
        pygame.draw.rect(screen, (140, 140, 220), self.rect, width=2, border_radius=3)
        
        if self.checked:
            pygame.draw.line(screen, (255, 255, 255), 
                           (self.x + 4, self.y + 10),
                           (self.x + 9, self.y + 16), 2)
            pygame.draw.line(screen, (255, 255, 255),
                           (self.x + 9, self.y + 16),
                           (self.x + 17, self.y + 4), 2)
        
        label_surface = self.font.render(self.label, True, (220, 220, 220))
        screen.blit(label_surface, (self.x + 30, self.y + 2))