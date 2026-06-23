import pygame
import json
import os
from scenes.menu.base_menu import BaseMenu, MY_FONT_PATH, MY_FONT_SIZE, Checkbox, BASE_DIR
from ui.slider import Slider


class SettingsMenu(BaseMenu):
    def __init__(self, game):
        super().__init__(game, "settings_menu")
        self.settings = self.load_settings()
        self.sliders = {}
        self.checkboxes = {}

        self.create_sliders()
        self.create_checkboxes()

    def save_and_exit(self):
        self.save_settings()
        self.go_back()

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
        from scenes.menu.base_menu import BASE_DIR
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
        for slider in self.sliders.values():
            if slider.handle_event(event, mouse_pos):
                self.apply_settings()
                return True

        for checkbox in self.checkboxes.values():
            if checkbox.handle_event(event, mouse_pos):
                if checkbox is self.checkboxes['fullscreen'] and checkbox.checked:
                    self.checkboxes['window'].checked = False
                elif checkbox is self.checkboxes['window'] and checkbox.checked:
                    self.checkboxes['fullscreen'].checked = False

                self.apply_settings()
                return True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.save_and_exit()
            return True

        return super().handle_event(event, mouse_pos, action, dt)

    def apply_settings(self):
        if not self.game:
            return

        if hasattr(self.game, 'music_volume'):
            self.game.music_volume = self.sliders['music_volume'].value / 100.0

        want_fullscreen = self.checkboxes['fullscreen'].checked
        current_fullscreen = getattr(self.game, 'fullscreen', False)

        if want_fullscreen != current_fullscreen:
            print(f"Переключаю fullscreen: {current_fullscreen} → {want_fullscreen}")
            try:
                self.game.toggle_fullscreen()
                self.settings['fullscreen'] = want_fullscreen
            except Exception as e:
                print(f"Ошибка переключения fullscreen: {e}")
                self.checkboxes['fullscreen'].checked = current_fullscreen
                self.checkboxes['window'].checked = not current_fullscreen

    def update(self, dt):
        pass

    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)

        title = self.title_font.render("SETTINGS", True, (200, 200, 255))
        screen.blit(title, (50, 50))

        display_label = self.label_font.render("Display", True, (200, 200, 200))
        screen.blit(display_label, (150, 170))

        audio_label = self.label_font.render("Audio", True, (200, 200, 200))
        screen.blit(audio_label, (450, 170))

        skip_label = self.label_font.render("Skip", True, (200, 200, 200))
        screen.blit(skip_label, (900, 170))

        for checkbox in self.checkboxes.values():
            checkbox.draw(screen, mouse_pos)

        for slider in self.sliders.values():
            slider.draw(screen)

        for button in self.buttons:
            button.draw(screen, mouse_pos)