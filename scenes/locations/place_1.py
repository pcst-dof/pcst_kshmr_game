import pygame
from scenes.scene import Scene
from assets.sprites.character import Character


class Place_1(Scene):
    """Комната спокойного клоуна."""

    def __init__(self, game):
        super().__init__("assets/images/background_1.jpg")
        self.game = game
        self.choice_active = False
        self.selected_choice = 0
        
        try:
            friend_states = {
                "clown_angry": "assets/images/clown_1/клоун 1.1.png",
                "clown_neutral": "assets/images/clown_1/клоун 1.2.png",
                "clown_happy": "assets/images/clown_1/клоун 1.3.png",
            }
            friend = Character(
                "Клоун",
                "assets/images/clown_1/клоун 1.1.png",
                -420,
                186,
                state_images=friend_states,
                default_state="clown_angry",
            )
            self.add_character(friend)
            self.friend_character = friend
            self.character_appeared = False
            self.appearance_timer = 0.0  
            self.appearance_duration = 1.5 
        except Exception as e:
            print(f"Ошибка загрузки спрайта персонажа: {e}")
            self.friend_character = None
            self.character_appeared = True

        self.dialogues = [
            {#1
                "type": "line",
                "speaker": "ГГ",
                "text": "Так, мы внутри. Ничего не видно..."
            },
            {#2
                "type": "line",
                "speaker": "Клоун",
                "text": "Добро пожаловать, добро пожаловать! Прошу, не стесняйтесь, места хватит для всех! Я Хирото, ваш покорный слуга!",
                "sprite": "clown_happy"
            },
            {#3
                "type": "line",
                "speaker": "Друг",
                "text": "Спасибо. Мы просто... хотели посмотреть."
            },
            {#4
                "type": "line",
                "speaker": "Хирото",
                "text": "Посмотреть? О, у нас тут на что посмотреть! А ты, мой серьезный друг, что скажешь? Зачем пришел в мой дом?",
                "sprite": "clown_happy"
            },
            {#5
                "type": "choice",
                "question": "Как ответить Хирото?",
                "options": [
                    {
                        "text": "«Хочу увидеть настоящее чудо. Удиви меня.»", 
                        "next": 5,
                        "relation_effect": "+1 (Веселье)",
                        "comment": "Плюс: Клоун в восторге, считает тебя «своим». Минус: Поощряешь его безумие, он теряет бдительность."
                    },
                    {
                        "text": "«Мы случайно забрели. Нам просто нужно пройти дальше.»", 
                        "next": 7,
                        "relation_effect": "0 (Нейтрально)",
                        "comment": "Плюс: Показываешь осторожность. Минус: Клоун находит тебя скучным, его интерес к тебе падает."
                    },
                    {
                        "text": "«Хватит ломать комедию. Ты знаешь, что тут происходит?»", 
                        "next": 9,
                        "relation_effect": "-1 (Раздражение)",
                        "comment": "Плюс: Сразу расставляешь границы. Минус: Клоун обижается, его безумие проявляется быстрее и агрессивнее."
                    }
                ]
            },
            {#6
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Чудо? О-о-о, я обожаю ценителей! Чудо требует жертв... то есть, аплодисментов! Ха-ха-ха!"
            },
            {#7
                "type": "jump",
                "next": 11
            },
            {#8
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Случайно? В моем-то коридоре? Ну-ну. Проходите, только не сворачивайте не туда. Стены тут... обидчивые."
            },
            {#9
                "type": "jump",
                "next": 11
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Комедию? Но жизнь и есть комедия, дружок! А ты такой... серьезный. Слишком серьезный. Это портит мне настроение!"
            },
            {
                "type": "jump",
                "next": 11
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Ладно, мы поняли. Слушай, а где..."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Эй? Ты чего отстал?"
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "...Он только что стоял прямо за мной."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "..."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Кто? Тот мальчик, который так громко стучал сердцем?"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Он ушел. Ему стало неинтересно. Или это мне стало неинтересно с ним. Уже не помню."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Что значит «ушел»? Где он?!"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "tilt_head",
                "text": "Ушел."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Люди постоянно куда-то уходят."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Он был здесь секунду назад!"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "sigh",
                "text": "Да..."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Забавно. Я тоже помню его здесь."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Где он?"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "smile",
                "text": "Не знаю."
            },
            {
                "type": "choice",
                "question": "Что делать?",
                "options": [
                    {
                        "text": "Осмотреть комнату",
                        "next": 100
                    },
                    {
                        "text": "Продолжить расспрашивать Клоуна",
                        "next": 120
                    }
                ]
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "..."
            },
            {
                "type": "line",
                "speaker": "Narrator",
                "text": "Вдоль стен лежат старые костюмы, разбитые прожекторы и пыльные ящики."
            },
            {
                "type": "line",
                "speaker": "Narrator",
                "text": "Позади Клепы неподвижно светится маленькая фигурка клоуна."
            },
            {
                "type": "line",
                "speaker": "Narrator",
                "text": "На полу видны свежие следы."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Следы?"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "tilt_head",
                "text": "Следы."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Они всегда куда-то ведут."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Это следы моего друга?"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "thinking",
                "text": "Твоего друга..."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "А как его звали?"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Ах да."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "text": "Теперь вспомнил."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "smile",
                "text": "Он очень громко боялся."
            },
            {
                "type": "line",
                "speaker": "Narrator",
                "text": "Кажется, светящаяся фигурка теперь стоит чуть ближе."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "smile",
                "text": "Впрочем, не буду пугать. Иди. И помни — я всегда смотрю."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Ты... ты просто маньяк."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "angry",
                "text": "Маньяк? *(Обижается, отступает)* Я — артист! Я — шоумен! Я — тот, кто делает темноту... ярче!"
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "sad",
                "text": "Но ладно. Обзывайся. Мне все равно. Главное — иди. Двери ждут. А я... я буду ждать здесь. Или там. Или везде."
            },
            {
                "type": "line",
                "speaker": "Хирото",
                "sprite": "clown_happy",
                "emotion": "smile",
                "text": "*(Исчезает в тени, но голос остается)* Удачи, дружок. Она тебе понадобится."
            },
            {
                "type": "line",
                "speaker": "ГГ",
                "text": "Черт... Ладно. Три двери. Надеюсь, он не соврал насчет друга.",
                "next_scene": "2"
            }
        ]

        self.current_dialogue = 0
        self.auto_advance_timer = 0  # для пропуска при удержании

    def get_current_dialogue(self):
        """Безопасное получение текущего диалога"""
        while 0 <= self.current_dialogue < len(self.dialogues) and self.dialogues[self.current_dialogue].get("type") == "jump":
            self.current_dialogue = self.dialogues[self.current_dialogue]["next"]

        if 0 <= self.current_dialogue < len(self.dialogues):
            return self.dialogues[self.current_dialogue]
        return None

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        """Обработка событий с поддержкой InputManager"""
        current = self.get_current_dialogue()
        if not current:
            return super().handle_event(event, mouse_pos, action, dt)

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
                    self._on_choice_made(self.selected_choice)
                    return True
                
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
                self._on_choice_made(self.selected_choice)
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
        # Анимация появления персонажа
        if self.friend_character and not self.character_appeared:
            self.appearance_timer += dt
            progress = min(self.appearance_timer / self.appearance_duration, 1.0)
            
            # Движение с права налево (из -420 в -20, чтобы край касался края)
            self.friend_character.x = -420 + progress * 400  # Движется вправо
            # Прозрачность: от 50 (затемнен) до 255 (видно)
            self.friend_character.opacity = int(130 + progress * 125)  # 130->255
            
            if progress >= 1.0:
                self.character_appeared = True
                self.friend_character.x = -20 
                self.friend_character.opacity = 255
        
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

    def _on_choice_made(self, choice_index):
        """Обработка выбора: меняем позицию персонажа в зависимости от выбора"""
        if not self.friend_character:
            return
        
        # смены позиции в зависимости от выбора (край касается края)
        if choice_index == 0:  # Первый вариант: "Это просто слухи."
            self.friend_character.x = -80  # Чуть левее
            self.friend_character.y = 186
            self.friend_character.set_state("clown_happy")
        elif choice_index == 1:  # Второй вариант: "Мне уже не по себе."
            self.friend_character.x = 40   # Чуть правее
            self.friend_character.y = 160
            self.friend_character.set_state("clown_neutral")
        elif choice_index == 2:  # Третий вариант: Промолчать
            self.friend_character.x = -20  # Центр
            self.friend_character.y = 186
            self.friend_character.set_state("clown_angry")
        
        # Обновляем rect после смены позиции
        if self.friend_character.rect:
            self.friend_character.rect.x = self.friend_character.x
            self.friend_character.rect.y = self.friend_character.y

    def _sync_friend_sprite(self):
        if not self.friend_character:
            return
        current = self.get_current_dialogue()
        if not current:
            return

        if current.get("speaker") == "Клоун":
            desired = current.get("sprite") or "clown_neutral"
            self.friend_character.set_state(desired)

    def draw(self, surface, mouse_pos=None):
        self._sync_friend_sprite()
        return super().draw(surface, mouse_pos)
