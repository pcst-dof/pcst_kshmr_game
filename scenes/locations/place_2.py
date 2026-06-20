# scenes/place_2.py
import pygame
from scenes.scene import Scene


class Place_2(Scene):
    """Эмоционально нестабильный клоун."""

    def __init__(self, game):
        super().__init__("assets/images/background_2.jpg")
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
                "next_scene": "1"  # Возврат на сцену 1
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
            self.game.change_scene("1")

    def draw(self, surface, mouse_pos=None):
        return super().draw(surface, mouse_pos)
