# scenes/scene.py
import os
import json
import pygame
from ui.menubar import MenuBar

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEFAULT_TEXT_FONT = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')

class Scene:
    def __init__(self, background_path=None):
        self.background = None
        self.auto_delay = 6.0
        if background_path:
            try:
                self.background = pygame.image.load(background_path)
            except Exception as e:
                print(f"Ошибка загрузки фона {background_path}: {e}")
        
        self.buttons = []
        self.characters = []
        self.dialogues = []
        self.menu_bar = None
        self.current_dialogue = 0
        self.dialogue_rect = pygame.Rect(40, 660, 1200, 230)
        self.selected_choice = 0
        self.text = ""
        
        # === НОВЫЕ ПЕРЕМЕННЫЕ ДЛЯ ФУНКЦИЙ ===
        self.history = []  # История диалогов для кнопки Back
        self.skip_mode = False  # Режим пропуска
        self.auto_mode = False  # Авторежим
        self.auto_timer = 0  # Таймер для авторежима
        self.auto_delay = 6000  # 6 секунд (в миллисекундах)
        
        try:
            self.font = pygame.font.Font(DEFAULT_TEXT_FONT, 32)
        except FileNotFoundError:
            print(f"шрифт {DEFAULT_TEXT_FONT} не найден! использую системный.")
            self.font = pygame.font.SysFont(None, 32)

    def add_button(self, button):
        self.buttons.append(button)

    def add_character(self, character):
        self.characters.append(character)

    def set_text(self, text):
        self.text = text
    
    def add_dialogue(self, dialogue):
        self.dialogues.append(dialogue)

    def get_current_dialogue(self):
        if 0 <= self.current_dialogue < len(self.dialogues):
            return self.dialogues[self.current_dialogue]
        return None
    
    def next_dialogue(self):
        # Сохраняем текущий диалог в историю
        current = self.get_current_dialogue()
        if current:
            self.history.append({
                "index": self.current_dialogue,
                "dialogue": current
            })
        
        if self.current_dialogue < len(self.dialogues) - 1:
            self.current_dialogue += 1
            # Если включен skip_mode и следующий диалог - это выбор, останавливаемся
            if self.skip_mode and self.dialogues[self.current_dialogue].get("type") == "choice":
                self.skip_mode = False
                print("Skip остановлен на выборе")
        else:
            print("Конец сцены")

    def previous_dialogue(self):
        """Возврат к предыдущему диалогу"""
        if self.history:
            last = self.history.pop()
            self.current_dialogue = last["index"]
            print(f"Возврат к диалогу {self.current_dialogue}")

    def wrap_text(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = (current_line + ' ' + word).strip() if current_line else word
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    def truncate_text(self, text, max_width):
        if self.font.size(text)[0] <= max_width:
            return text
        ellipsis = '...'
        while text and self.font.size(text + ellipsis)[0] > max_width:
            text = text[:-1]
        return text + ellipsis if text else ellipsis

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """Обработка событий"""

                # Обработка кликов по нижней панели меню
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouse_pos:
                footer_y = self.game.LOGICAL_H - 40
                menu_items = ["Back", "History", "Skip", "Auto", "Save", "Q.Save", "Q.Load", "Prefs"]
                spacing = 80
                start_x = (self.game.LOGICAL_W - spacing * len(menu_items)) // 2
                
                for i, item in enumerate(menu_items):
                    item_x = start_x + i * spacing
                    item_width = 80
                    item_rect = pygame.Rect(item_x, footer_y - 10, item_width, 25)
                    
                    if item_rect.collidepoint(mouse_pos):
                        if item == "Back":
                            self.previous_dialogue()
                        elif item == "History":
                            self.show_history()
                        elif item == "Skip":
                            self.skip_mode = True
                            print("Skip режим включен")
                        elif item == "Auto":
                            self.auto_mode = not self.auto_mode
                            if self.auto_mode:
                                self.auto_timer = 0
                            print(f"Auto режим: {'ВКЛ' if self.auto_mode else 'ВЫКЛ'}")
                        elif item == "Save":
                            self.save_game()
                        elif item == "Q.Save":
                            self.quick_save()
                        elif item == "Q.Load":
                            self.quick_load()
                        elif item == "Prefs":
                            self.open_preferences()
                        return True
                    
        # Отладка
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"[Scene] Клик: mouse_pos={mouse_pos}, dialogue={self.current_dialogue}")
        
        # Кнопки сцены
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None:
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True
        
        # === Обработка кнопок меню ===
        if self.menu_bar:
            clicked = self.menu_bar.handle_event(event, mouse_pos)
            if clicked:
                print(f"✓ Нажата кнопка: {clicked}")
                if clicked == "Back":
                    self.previous_dialogue()
                elif clicked == "History":
                    self.show_history()
                elif clicked == "Skip":
                    self.skip_mode = True
                    print("Skip режим включен")
                elif clicked == "Auto":
                    self.auto_mode = not self.auto_mode
                    if self.auto_mode:
                        self.auto_timer = 0
                    print(f"Auto режим: {'ВКЛ' if self.auto_mode else 'ВЫКЛ'}")
                elif clicked == "Save":
                    self.save_game()
                elif clicked == "Q.Save":
                    self.quick_save()
                elif clicked == "Q.Load":
                    self.quick_load()
                elif clicked == "Prefs":
                    self.open_preferences()
                return True
        
        # Переход к следующему диалогу
        if action == 'advance' and event.type != pygame.MOUSEBUTTONDOWN:
            self.next_dialogue()
            return True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_dialogue()
                return True
        
        return False

    def update(self, dt):
        """Обновление каждый кадр"""
        # Авторежим
        if self.auto_mode:
            self.auto_timer += dt
            if self.auto_timer >= self.auto_delay:
                self.auto_timer = 0
                self.next_dialogue()
                print(f"Auto: переход к диалогу {self.current_dialogue}")

    def draw(self, screen, mouse_pos=None):
        # === ФОН ===
        if self.background:
            bg_w, bg_h = self.background.get_size()
            screen_w, screen_h = screen.get_size()
            scale = min(screen_w / bg_w, screen_h / bg_h)
            new_w = int(bg_w * scale)
            new_h = int(bg_h * scale)

            background_scaled = pygame.transform.smoothscale(
                self.background, (new_w, new_h)
            )

            offset_x = (screen_w - new_w) // 2
            offset_y = (screen_h - new_h) // 2

            screen.fill((10, 10, 10))
            screen.blit(background_scaled, (offset_x, offset_y))

            overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
        else:
            screen.fill((10, 10, 10))

        # === ПЕРСОНАЖИ ===
        screen_w, screen_h = screen.get_size()
        
        for character in self.characters:
            character.scale_to_screen(screen_w, screen_h, scale_factor=0.85)
            character.draw(screen)

        for button in self.buttons:
            button.draw(screen, mouse_pos)

        current = self.get_current_dialogue()
        if not current:
            return

        # === ДИАЛОГОВОЕ ОКНО ===
        dx = self.dialogue_rect.x
        dy = self.dialogue_rect.y
        dw = self.dialogue_rect.width
        dh = self.dialogue_rect.height

        # Тень
        for offset in range(3, 0, -1):
            shadow = pygame.Surface((dw + offset * 2, dh + offset * 2), pygame.SRCALPHA)
            alpha = 80 - offset * 15
            pygame.draw.rect(shadow, (20, 10, 40, alpha), shadow.get_rect(), border_radius=12)
            screen.blit(shadow, (dx - offset, dy - offset))

        # Фон
        dialogue_bg = pygame.Surface((dw, dh), pygame.SRCALPHA)
        for i in range(dh):
            ratio = i / dh
            r = int(30 * (1 - ratio) + 10 * ratio)
            g = int(20 * (1 - ratio) + 5 * ratio)
            b = int(50 * (1 - ratio) + 20 * ratio)
            pygame.draw.line(dialogue_bg, (r, g, b, 220), (0, i), (dw, i))
        screen.blit(dialogue_bg, (dx, dy))

        # Обводка
        pygame.draw.rect(screen, (120, 80, 200, 180), (dx, dy, dw, dh), width=2, border_radius=12)
        pygame.draw.rect(screen, (180, 140, 255, 100), (dx + 1, dy + 1, dw - 2, dh - 2), width=1, border_radius=11)

        # Полоса для имени
        bar_height = 45
        bar_rect = pygame.Rect(dx + 15, dy + 10, dw - 30, bar_height)
        pygame.draw.rect(screen, (15, 10, 30, 200), bar_rect, border_radius=8)
        pygame.draw.rect(screen, (100, 60, 180, 150), bar_rect, width=1, border_radius=8)

        # Уголки
        pygame.draw.polygon(screen, (140, 100, 220, 200), [
            (dx + 15, dy + bar_height + 5),
            (dx + 25, dy + bar_height - 5),
            (dx + 15, dy + bar_height - 5)
        ])
        pygame.draw.polygon(screen, (140, 100, 220, 200), [
            (dx + dw - 15, dy + bar_height + 5),
            (dx + dw - 25, dy + bar_height - 5),
            (dx + dw - 15, dy + bar_height - 5)
        ])

        if current["type"] == "line":
            player_name = "Player"
            if hasattr(self, 'game') and getattr(self.game, 'player_name', None):
                player_name = self.game.player_name

            speaker = current.get("speaker", "")
            text = current.get("text", "")
            for token in ("{player}", "{player_name}", "ГГ", "Гг", "гг", "GG", "Gg", "gg"):
                speaker = speaker.replace(token, player_name)
                text = text.replace(token, player_name)

            speaker = self.truncate_text(speaker, bar_rect.width - 40)
            speaker_surface = self.font.render(speaker, True, (220, 180, 255))
            speaker_y = dy + 10 + (bar_height - speaker_surface.get_height()) // 2
            screen.blit(speaker_surface, (bar_rect.x + 20, speaker_y))

            max_width = dw - 60
            lines = self.wrap_text(text, max_width)

            x = dx + 30
            y = dy + 70
            line_height = 38
            for line in lines:
                shadow_text = self.font.render(line, True, (0, 0, 0))
                screen.blit(shadow_text, (x + 2, y + 2))
                text_surface = self.font.render(line, True, (240, 230, 255))
                screen.blit(text_surface, (x, y))
                y += line_height
                if y > dy + dh - 45:
                    break

        elif current["type"] == "choice":
            player_name = "Player"
            if hasattr(self, 'game') and getattr(self.game, 'player_name', None):
                player_name = self.game.player_name

            question = current.get("question", "")
            for token in ("{player}", "{player_name}", "ГГ", "Гг", "гг", "GG", "Gg", "gg"):
                question = question.replace(token, player_name)

            question = self.truncate_text(question, bar_rect.width - 40)
            question_surface = self.font.render(question, True, (220, 180, 255))
            question_y = dy + 10 + (bar_height - question_surface.get_height()) // 2
            screen.blit(question_surface, (bar_rect.x + 20, question_y))

            y = dy + 70
            for i, option in enumerate(current.get("options", [])):
                opt_text = option.get("text", "")
                for token in ("{player}", "{player_name}", "ГГ", "Гг", "гг", "GG", "Gg", "gg"):
                    opt_text = opt_text.replace(token, player_name)

                if i == self.selected_choice:
                    choice_bg = pygame.Surface((dw - 80, 45), pygame.SRCALPHA)
                    pygame.draw.rect(choice_bg, (100, 60, 180, 150), choice_bg.get_rect(), border_radius=8)
                    screen.blit(choice_bg, (dx + 40, y - 5))
                    pygame.draw.rect(screen, (180, 140, 255, 200), (dx + 40, y - 5, dw - 80, 45), width=2, border_radius=8)
                    prefix = "► "
                    color = (255, 250, 255)
                else:
                    prefix = "  "
                    color = (200, 190, 220)

                opt_text = self.truncate_text(opt_text, dw - 120)
                option_shadow = self.font.render(prefix + opt_text, True, (0, 0, 0))
                screen.blit(option_shadow, (dx + 52, y + 2))
                option_surface = self.font.render(prefix + opt_text, True, color)
                screen.blit(option_surface, (dx + 50, y))
                y += 55

        # === НИЖНЯЯ ПАНЕЛЬ МЕНЮ ===
        self._draw_bottom_menu(screen, mouse_pos)

    def _draw_bottom_menu(self, screen, mouse_pos):
        """Рисует нижнюю панель меню (стиль стартовой сцены)"""
        footer_y = self.game.LOGICAL_H - 60
        menu_font = pygame.font.SysFont(None, 20)
        menu_items = ["Back", "History", "Skip", "Auto", "Save", "Q.Save", "Q.Load", "Prefs"]
        spacing = 80
        start_x = (self.game.LOGICAL_W - spacing * len(menu_items)) // 2
        
        # Проверяем наведение мыши
        hovered_item = None
        if mouse_pos:
            for i, item in enumerate(menu_items):
                item_x = start_x + i * spacing
                item_rect = pygame.Rect(item_x, footer_y - 10, 
                                       menu_font.size(item)[0] + 10, 25)
                if item_rect.collidepoint(mouse_pos):
                    hovered_item = i
                    break
        
        # Рисуем элементы
        for i, item in enumerate(menu_items):
            item_x = start_x + i * spacing
            
            # Цвет: светлее при наведении
            if i == hovered_item:
                color = (200, 200, 200)  # светлее
                # Лёгкая тень
                shadow_surf = menu_font.render(item, True, (0, 0, 0))
                screen.blit(shadow_surf, (item_x + 1, footer_y + 1))
            else:
                color = (140, 140, 140)  # обычный
            
            item_surf = menu_font.render(item, True, color)
            screen.blit(item_surf, (item_x, footer_y))

    # === МЕТОДЫ ДЛЯ КНОПОК ===
    
    def show_history(self):
        """Показать историю диалогов"""
        print(f"История: {len(self.history)} записей")
        for i, entry in enumerate(self.history[-5:], 1):  # Показываем последние 5
            print(f"{i}. Диалог #{entry['index']}: {entry['dialogue'].get('text', '')[:50]}...")

    def save_game(self):
        """Сохранение прогресса"""
        try:
            save_data = {
                "scene": self.__class__.__name__,
                "current_dialogue": self.current_dialogue,
                "history_length": len(self.history),
                "timestamp": str(pygame.time.get_ticks())
            }
            
            save_path = os.path.join(BASE_DIR, "saves", "save.json")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print("✓ Игра сохранена")
        except Exception as e:
            print(f"✗ Ошибка сохранения: {e}")

    def quick_save(self):
        """Быстрое сохранение с выходом в меню"""
        try:
            save_data = {
                "scene": self.__class__.__name__,
                "current_dialogue": self.current_dialogue,
                "history": self.history,
                "skip_mode": self.skip_mode,
                "auto_mode": self.auto_mode,
                "timestamp": str(pygame.time.get_ticks())
            }
            
            save_path = os.path.join(BASE_DIR, "saves", "quick_save.json")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print("✓ Быстрое сохранение выполнено")
            # Здесь код для выхода в меню:
            # self.game.change_scene("main_menu")
        except Exception as e:
            print(f"✗ Ошибка быстрого сохранения: {e}")

    def quick_load(self):
        """Быстрая загрузка с выходом в меню"""
        try:
            save_path = os.path.join(BASE_DIR, "saves", "quick_save.json")
            
            if not os.path.exists(save_path):
                print("✗ Нет быстрого сохранения")
                return
            
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            self.current_dialogue = save_data.get("current_dialogue", 0)
            self.history = save_data.get("history", [])
            self.skip_mode = save_data.get("skip_mode", False)
            self.auto_mode = save_data.get("auto_mode", False)
            
            print("✓ Быстрая загрузка выполнена")
            # Здесь код для выхода в меню:
            # self.game.change_scene("main_menu")
        except Exception as e:
            print(f"✗ Ошибка быстрой загрузки: {e}")

    def open_preferences(self):
        """Открыть настройки"""
        print("Открыть настройки...")
        # Здесь код для открытия окна настроек:
        # self.game.show_settings()