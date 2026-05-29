# scenes/scene.py
import os
import pygame

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEFAULT_TEXT_FONT = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')

class Scene:
    def __init__(self, background_path=None):
        self.background = None
        if background_path:
            try:
                self.background = pygame.image.load(background_path)
            except Exception as e:
                print(f"Ошибка загрузки фона {background_path}: {e}")
        self.buttons = []
        self.characters = []
        self.dialogues = []
        self.current_dialogue = 0
        self.dialogue_rect = pygame.Rect(40, 500, 1200, 200)
        self.text = ""
        try:
            self.font = pygame.font.Font(DEFAULT_TEXT_FONT, 42)
        except FileNotFoundError:
            print(f"шрифт {DEFAULT_TEXT_FONT} не найден! использую системный.")
            self.font = pygame.font.SysFont(None, 42)

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
        if self.current_dialogue < len(self.dialogues) - 1:
            self.current_dialogue += 1
        else:
            print("Конец сцены")

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

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """
        Обработка событий — кнопки ПЕРЕД диалогом!
        """
        # === 1. Сначала проверяем клики по кнопкам (ВАЖНО!) ===
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None:
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True  # Кнопка обработана — дальше не идём
        
        # === 2. Теперь проверяем действия от InputManager ===
        # Но только если это не клик мышью (чтобы не дублировать)
        if action == 'advance' and event.type != pygame.MOUSEBUTTONDOWN:
            self.next_dialogue()
            return True
        
        # === 3. Старая логика для клавиатуры ===
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.next_dialogue()
                return True
        
        return False

    def update(self, dt):
        """Вызывается каждый кадр"""
        pass

    def draw(self, screen, mouse_pos=None):
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

        for character in self.characters:
            character.draw(screen)

        current = self.get_current_dialogue()

        for button in self.buttons:
            button.draw(screen, mouse_pos)

        if not current:
            return

        pygame.draw.rect(screen, (20, 20, 20), self.dialogue_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.dialogue_rect, 3)

        if current["type"] == "line":
            speaker = current.get("speaker", "")
            text = current.get("text", "")

            speaker_surface = self.font.render(speaker, True, (255, 255, 255))
            screen.blit(speaker_surface, (self.dialogue_rect.x + 30, self.dialogue_rect.y + 15))

            max_width = self.dialogue_rect.width - 60
            lines = self.wrap_text(text, max_width)

            x = self.dialogue_rect.x + 30
            y = self.dialogue_rect.y + 70
            for line in lines:
                text_surface = self.font.render(line, True, (220, 220, 220))
                screen.blit(text_surface, (x, y))
                y += 35
                if y > self.dialogue_rect.bottom - 40:
                    break

        elif current["type"] == "choice":
            question = current["question"]
            question_surface = self.font.render(question, True, (255, 255, 255))
            screen.blit(question_surface, (self.dialogue_rect.x + 30, self.dialogue_rect.y + 20))

            y = self.dialogue_rect.y + 80
            for i, option in enumerate(current["options"]):
                prefix = "> " if i == self.selected_choice else "  "
                option_surface = self.font.render(prefix + option["text"], True, (220, 220, 220))
                screen.blit(option_surface, (self.dialogue_rect.x + 50, y))
                y += 45