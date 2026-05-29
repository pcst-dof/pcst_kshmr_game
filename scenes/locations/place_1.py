# scenes/place_1.py
import pygame
from scenes.scene import Scene


class Place_1(Scene):
    """Комната спокойного клоуна."""

    def __init__(self, game):
        super().__init__("assets/images/background_1.jpg")
        self.game = game
        self.choice_active = False
        self.selected_choice = 0
        self.dialogues = [
            {
                "type": "line",
                "speaker": "Друг",
                "text": "Ну... вот оно."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Выглядит хуже, чем на фотках."
            },
            {
                "type": "line",
                "speaker": "Друг",
                "text": "Ты ведь тоже слышал все эти истории?"
            },
            {
                "type": "choice",
                "question": "Как ответить?",
                "options": [
                    {"text": "«Это просто слухи.»", "next": 4},
                    {"text": "«Мне уже не по себе.»", "next": 6},
                    {"text": "Промолчать", "next": 8}
                ]
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Это просто слухи."
            },
            {
                "type": "line",
                "speaker": "Друг",
                "text": "Надеюсь."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Мне уже не по себе."
            },
            {
                "type": "line",
                "speaker": "Друг",
                "text": "Вот и мне тоже."
            },
            {
                "type": "line",
                "speaker": "Друг",
                "text": "...Ты чего молчишь?"
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Пошли уже.",
                "next_scene": "2"
            }
        ]
        self.current_dialogue = 0
        self.auto_advance_timer = 0  # для пропуска при удержании

    def get_current_dialogue(self):
        """Безопасное получение текущего диалога"""
        if 0 <= self.current_dialogue < len(self.dialogues):
            return self.dialogues[self.current_dialogue]
        return None

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """Обработка событий с поддержкой InputManager"""
        current = self.get_current_dialogue()
        if not current:
            return super().handle_event(event, mouse_pos, action, dt)

        
        # === СТАРАЯ ЛОГИКА (оставляем для совместимости) ===
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current["type"] == "line":
                if "next_scene" in current:
                    self.game.change_scene(current["next_scene"])
                    return True
                if "next" in current:
                    self.current_dialogue = current["next"]
                    return True
                self.next_dialogue()
                return True
            
            if current["type"] == "choice":
                if event.key == pygame.K_UP:
                    self.selected_choice = max(0, self.selected_choice - 1)
                    return True
                elif event.key == pygame.K_DOWN:
                    self.selected_choice = min(len(current["options"]) - 1, self.selected_choice + 1)
                    return True
                elif event.key == pygame.K_RETURN:
                    option = current["options"][self.selected_choice]
                    self.current_dialogue = option["next"]
                    return True
                
        # === ОБРАБОТКА ДЕЙСТВИЙ ОТ INPUTMANAGER ===
        # Продвижение диалога (работает для Enter, Space, ЛКМ)
        if action == 'advance':
            if current["type"] == "line":
                if "next_scene" in current:
                    self.game.change_scene(current["next_scene"])
                    return True
                if "next" in current:
                    self.current_dialogue = current["next"]
                    return True
                self.next_dialogue()
                return True
            
            elif current["type"] == "choice":
                # Если есть выбор — нажатие advance подтверждает выбранный вариант
                option = current["options"][self.selected_choice]
                self.current_dialogue = option["next"]
                return True

        # Навигация по выбору (стрелки)
        if current["type"] == "choice":
            if action == 'nav_up':
                self.selected_choice = max(0, self.selected_choice - 1)
                return True
            if action == 'nav_down':
                self.selected_choice = min(len(current["options"]) - 1, self.selected_choice + 1)
                return True

        # Меню игры (Escape / ПКМ)
        if action == 'menu':
            self.game.change_scene('main_menu')
            return True

        

        # Кнопки из базового класса (Вернуться и т.д.)
        return super().handle_event(event, mouse_pos, action, dt)

    def update(self, dt):
        """Вызывается каждый кадр — для авто-пропуска при удержании"""
        # Если игрок удерживает клавишу пропуска — ускоряем диалог
        if self.game.input_manager.is_skipping():
            self.auto_advance_timer += dt
            if self.auto_advance_timer >= 0.05:  # 50мс между шагами
                self.auto_advance_timer = 0
                current = self.get_current_dialogue()
                if current and current["type"] == "line":
                    if "next_scene" in current:
                        self.game.change_scene(current["next_scene"])
                        return
                    if "next" in current:
                        self.current_dialogue = current["next"]
                        return
                    self.next_dialogue()

    def next_dialogue(self):
        """Переход к следующей реплике"""
        if self.current_dialogue < len(self.dialogues) - 1:
            self.current_dialogue += 1
        else:
            self.game.change_scene("2")

    def draw(self, surface, mouse_pos=None):
        """Отрисовка сцены — без дублирования диалога"""
        
        # === Рисуем фон и оверлей (как в базовом классе) ===
        if self.background:
            bg_w, bg_h = self.background.get_size()
            screen_w, screen_h = surface.get_size()
            scale = min(screen_w / bg_w, screen_h / bg_h)
            new_w = int(bg_w * scale)
            new_h = int(bg_h * scale)
            
            background_scaled = pygame.transform.smoothscale(self.background, (new_w, new_h))
            offset_x = (screen_w - new_w) // 2
            offset_y = (screen_h - new_h) // 2
            
            surface.fill((10, 10, 10))
            surface.blit(background_scaled, (offset_x, offset_y))
            
            overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            surface.blit(overlay, (0, 0))
        else:
            surface.fill((10, 10, 10))
        
        # === Рисуем персонажей ===
        for character in self.characters:
            character.draw(surface)
        
        # === Рисуем кнопки (но не диалог из базового класса!) ===
        for button in self.buttons:
            button.draw(surface, mouse_pos)
        
        # === Рисуем диалог ТОЛЬКО здесь (один раз!) ===
        current = self.get_current_dialogue()
        if not current:
            return
        
        # Фон диалогового окна
        pygame.draw.rect(surface, (20, 20, 20), self.dialogue_rect)
        pygame.draw.rect(surface, (255, 255, 255), self.dialogue_rect, 3)
        
        if current["type"] == "line":
            speaker = current.get("speaker", "")
            text = current.get("text", "")
            
            speaker_surface = self.font.render(speaker, True, (255, 255, 255))
            surface.blit(speaker_surface, (self.dialogue_rect.x + 30, self.dialogue_rect.y + 15))
            
            max_width = self.dialogue_rect.width - 60
            lines = self.wrap_text(text, max_width)
            
            x = self.dialogue_rect.x + 30
            y = self.dialogue_rect.y + 70
            for line in lines:
                text_surface = self.font.render(line, True, (220, 220, 220))
                surface.blit(text_surface, (x, y))
                y += 35
                if y > self.dialogue_rect.bottom - 40:
                    break
                    
        elif current["type"] == "choice":
            question = current["question"]
            question_surface = self.font.render(question, True, (255, 255, 255))
            surface.blit(question_surface, (self.dialogue_rect.x + 30, self.dialogue_rect.y + 20))
            
            y = self.dialogue_rect.y + 80
            for i, option in enumerate(current["options"]):
                prefix = "> " if i == self.selected_choice else "  "
                option_surface = self.font.render(prefix + option["text"], True, (220, 220, 220))
                surface.blit(option_surface, (self.dialogue_rect.x + 50, y))
                y += 45