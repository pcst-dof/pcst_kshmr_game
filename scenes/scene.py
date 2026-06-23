import os
import json
import pygame

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEFAULT_TEXT_FONT = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')

MENU_ITEMS = ["Back", "History", "Skip", "Auto", "Save", "Q.Save", "Q.Load", "Prefs"]
MENU_SPACING = 80
MENU_FOOTER_OFFSET = 25


class Scene:
    def __init__(self, background_path=None, scene_name=''):
        self.name = scene_name
        self.background = None
        self.auto_delay = 1.0
        if background_path:
            try:
                self.background = pygame.image.load(background_path)
            except Exception as e:
                print(f"Ошибка загрузки фона {background_path}: {e}")
        
        self.buttons = []
        self.characters = []
        self.dialogues = []
        self.current_dialogue = 0
        self.dialogue_rect = pygame.Rect(40, 660, 1200, 230)
        self.selected_choice = 0
        self.text = ""
        self.show_bottom_menu = False
        
        # Функции меню
        self.history = []
        self.skip_mode = False
        self.auto_mode = False
        self.auto_timer = 0
        
        # Временная блокировка advance после клика по нижней панели
        self._ignore_advance_until = 0
        
        try:
            self.font = pygame.font.Font(DEFAULT_TEXT_FONT, 32)
        except FileNotFoundError:
            print(f"шрифт {DEFAULT_TEXT_FONT} не найден! использую системный.")
            self.font = pygame.font.SysFont(None, 32)
        
        self.menu_font = pygame.font.SysFont(None, 20)

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
        self.history.append(self.current_dialogue)

        if self.current_dialogue < len(self.dialogues) - 1:
            self.current_dialogue += 1

            current = self.get_current_dialogue()

            if (
                self.skip_mode
                and current
                and current.get("type") == "choice"
            ):
                self.skip_mode = False

        else:
            print("Конец сцены")

    def previous_dialogue(self):
        if self.current_dialogue > 0:
            self.current_dialogue -= 1

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

    def _get_menu_item_rects(self):
        """Возвращает список кортежей (item_name, rect) для кнопок нижней панели."""
        footer_y = self.game.LOGICAL_H - MENU_FOOTER_OFFSET
        start_x = (self.game.LOGICAL_W - MENU_SPACING * len(MENU_ITEMS)) // 2
        
        rects = []
        for i, item in enumerate(MENU_ITEMS):
            item_x = start_x + i * MENU_SPACING
            item_width = MENU_SPACING
            item_height = 30
            item_rect = pygame.Rect(item_x - 5, footer_y - 8, item_width, item_height)
            rects.append((item, item_rect))
        
        return rects
    
    def _handle_bottom_menu_click(self, mouse_pos):
        """Обработка клика по нижней панели. Возвращает True если клик был обработан."""
        if not mouse_pos:
            return False
        
        for item, item_rect in self._get_menu_item_rects():
            if item_rect.collidepoint(mouse_pos):
                # блок advance на 200мс, чтобы отпускание мыши не продвинуло диалог
                self._ignore_advance_until = pygame.time.get_ticks() + 200
                
                if item == "Back":
                    if self.history:
                        self.previous_dialogue()
                elif item == "History":
                    self.show_history()
                elif item == "Skip":
                    self.skip_mode = not self.skip_mode

                elif item == "Auto":
                    self.auto_mode = not self.auto_mode
                    if self.auto_mode:
                        self.auto_timer = 0
                elif item == "Save":
                    self.save_game()
                elif item == "Q.Save":
                    self.quick_save()
                elif item == "Q.Load":
                    self.quick_load()
                elif item == "Prefs":
                    self.open_preferences()
                return True
        
        return False
    
    def _draw_bottom_menu(self, screen, mouse_pos):
        """Рисует нижнюю панель меню"""
        footer_y = self.game.LOGICAL_H - MENU_FOOTER_OFFSET
        menu_rects = self._get_menu_item_rects()
        
        hovered_item = None
        if mouse_pos:
            for i, (item, item_rect) in enumerate(menu_rects):
                if item_rect.collidepoint(mouse_pos):
                    hovered_item = i
                    break
        
        for i, (item, item_rect) in enumerate(menu_rects):
            item_x = item_rect.x + 5
            
            if i == hovered_item:
                color = (220, 220, 220)
                shadow_surf = self.menu_font.render(item, True, (0, 0, 0))
                screen.blit(shadow_surf, (item_x + 1, footer_y + 1))
            else:
                color = (140, 140, 140)
            
            item_surf = self.menu_font.render(item, True, color)
            screen.blit(item_surf, (item_x, footer_y))

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """Обработка событий"""
        
        # Клики по нижней панели меню
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.show_bottom_menu:
                if self._handle_bottom_menu_click(mouse_pos):
                    return True
        
        # Кнопки сцены
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None:
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True
        
        # Пробел — следующий диалог
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_dialogue()
                return True
        
        # Advance action 
        if action == 'advance':
            if pygame.time.get_ticks() < self._ignore_advance_until:
                return True
            self.next_dialogue()
            return True
        
        return False

    def update(self, dt):
        current = self.get_current_dialogue()

        if self.skip_mode:

            while not current.get("type") == "choice":
                self.next_dialogue()
                current = self.get_current_dialogue()
            self.skip_mode = False

        if self.auto_mode:

            if current and current.get("type") == "choice":
                self.auto_mode = False

            else:
                self.auto_timer += dt

                if self.auto_timer >= self.auto_delay:
                    self.auto_timer = 0
                    self.next_dialogue()

    def draw(self, screen, mouse_pos=None):
        # фон
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

        # спруты
        screen_w, screen_h = screen.get_size()
        
        for character in self.characters:
            character.scale_to_screen(screen_w, screen_h, scale_factor=0.85)
            character.draw(screen)

        for button in self.buttons:
            button.draw(screen, mouse_pos)

        current = self.get_current_dialogue()
        
        if current:
            self._draw_dialogue(screen, current)

        # нижняя панель
        if self.show_bottom_menu:
            self._draw_bottom_menu(screen, mouse_pos)
    
    def _draw_dialogue(self, screen, current):
        """Отрисовка диалогового окна"""
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

    def show_history(self):
        print("\n===== HISTORY =====")

        start = max(0, self.current_dialogue - 20)

        for i in range(start, self.current_dialogue + 1):
            dialogue = self.dialogues[i]

            if dialogue["type"] == "line":
                speaker = dialogue.get("speaker", "")
                text = dialogue.get("text", "")

                print(f"{speaker}: {text}")

        print("===================\n")

    def save_game(self):
        """Открыть меню сохранений"""
        if hasattr(self, 'game') and self.game:
            screenshot = self.game.virtual_screen.copy()
            game_state = self.game.get_game_state()
            self.game.scenes['save_menu'].game_state_to_save = game_state
            self.game.scenes['save_menu'].screenshot_to_save = screenshot
            self.game.scenes['save_menu'].previous_scene = self.name

            self.game.change_scene("save_menu")

    def quick_save(self):
        """Быстрое сохранение в слот 1"""
        if not hasattr(self, 'game') or not self.game:
            return

        screenshot = pygame.Surface(
            (self.game.LOGICAL_W, self.game.LOGICAL_H)
        )

        self.draw(screenshot)

        self.game.save_game(
            slot=1,
            screenshot=screenshot
        )

        print("Quick Save")

    def quick_load(self):
        """Загрузка из слота 1"""
        from utils.save_manager import SaveManager

        save_manager = SaveManager()

        game_state = save_manager.load_save(1)

        if not game_state:
            print("✗ Нет быстрого сохранения")
            return

        self.game.load_state(game_state)

        scene_name = game_state.get(
            "current_scene",
            "main_menu"
        )

        self.game.change_scene(scene_name)

        self.current_dialogue = game_state.get('current_dialogue', 0)

        print("Quick Load")

    def open_preferences(self):
        """Открыть настройки"""
        print("Открыть настройки...")
        if hasattr(self, 'game') and self.game:
            self.game.scenes['settings_menu'].previous_scene = self.name
            self.game.change_scene("settings_menu")