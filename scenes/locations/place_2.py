from scenes.base_dialogue_scene import BaseDialogueScene
from assets.sprites.character import Character


class Place_2(BaseDialogueScene):
    """Комната умного клоуна."""

    CLOWN_ID = "clown_2"
    ABEL_ID = "abel"
    NEXT_SCENE = None  # Разные концовки задаются в самих диалогах

    SPRITE_ID = None
    RELATIONSHIP_PARAMS = {}

    DIALOGUES = [
        {
            "type": "line",
            "speaker": "***",
            "text": "*Дверь за спиной закрывается сама.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*В центре комнаты — доски с формулами, схемы графов, исписанные листы.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун сидит спиной. Что-то пишет. Даже не оборачивается.*"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Если человек заходит в комнату и не здоровается — он невежливый."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Если человек заходит в комнату и здоровается с пустотой — он глупый."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Какой вариант выберешь?"
        },
        {
            "type": "choice",
            "question": "Как ответить?",
            "options": [
                {
                    "text": "«Здравствуйте.»",
                    "next": 11,
                    "intellect": -1,
                    "respect": -1
                },
                {
                    "text": "Промолчать.",
                    "next": 15,
                    "intellect": 0
                },
                {
                    "text": "«Есть третий вариант.»",
                    "next": 19,
                    "intellect": 2,
                    "unconventional": 3
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Здравствуйте."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун продолжает писать. Не оборачивается.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Предсказуемо."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Как и большинство посетителей."
        },
        {
            "type": "jump",
            "next": 23
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*ГГ молчит.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун делает пометку в блокноте.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Молчание — это тоже ответ."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Но не самый интересный."
        },
        {
            "type": "jump",
            "next": 23
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Есть третий вариант."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун наконец поворачивает голову.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Хорошо."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Назови его."
        },
        {
            "type": "jump",
            "next": 23
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Брат сказал, что ты интересный."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "И?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Я пока не уверен."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Он впервые поднимает взгляд.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Докажи."
        },
        {
            "type": "choice",
            "question": "Как ответить?",
            "options": [
                {
                    "text": "«Я никому ничего не доказываю.»",
                    "next": 32,
                    "respect": 3,
                    "unconventional": 2
                },
                {
                    "text": "«Как именно?»",
                    "next": 36,
                    "intellect": 1,
                    "respect": 1
                },
                {
                    "text": "«А если не хочу?»",
                    "next": 40,
                    "respect": -2,
                    "unconventional": 1
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Я никому ничего не доказываю."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун долго смотрит.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Хорошо."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что хорошо?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Хоть один человек сегодня сказал это."
        },
        {
            "type": "jump",
            "next": 44
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Как именно?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Уже лучше."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Большинство спрашивает «зачем». Ты спросил «как»."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Это разные вещи."
        },
        {
            "type": "jump",
            "next": 44
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "А если не хочу?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Тогда дверь позади тебя."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун смотрит на дверь.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Хотя нет."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Уже не дверь."
        },
        {
            "type": "jump",
            "next": 44
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Представь граф."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Вершины — люди."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Рёбра — связи между ними."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Он берёт мел.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Если удалить все рёбра."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Что останется?"
        },
        {
            "type": "choice",
            "question": "Что ответить?",
            "options": [
                {
                    "text": "«Ничего.»",
                    "next": 57,
                    "intellect": -2
                },
                {
                    "text": "«Люди.»",
                    "next": 60,
                    "intellect": 1
                },
                {
                    "text": "«Зависит от графа.»",
                    "next": 63,
                    "intellect": 0,
                    "unconventional": 1
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Ничего."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун морщится.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Люди никуда не делись."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Исчезли только связи."
        },
        {
            "type": "jump",
            "next": 66
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Люди."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Очевидно."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Но верно."
        },
        {
            "type": "jump",
            "next": 66
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Зависит от графа."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Нет."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "В этот раз не зависит."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Но мысль интересная."
        },
        {
            "type": "jump",
            "next": 66
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Что хуже?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Ошибиться."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Или отказаться отвечать?"
        },
        {
            "type": "choice",
            "question": "Что ответить?",
            "options": [
                {
                    "text": "«Ошибиться.»",
                    "next": 77,
                    "intellect": -1
                },
                {
                    "text": "«Отказаться отвечать.»",
                    "next": 81,
                    "respect": 2,
                    "intellect": 1
                },
                {
                    "text": "«Зависит от ситуации.»",
                    "next": 85,
                    "unconventional": 1
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Ошибиться."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Нет."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Ошибка создаёт информацию."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Молчание — нет."
        },
        {
            "type": "jump",
            "next": 89
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Отказаться отвечать."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Именно."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Молчание — это выбор не генерировать данные."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "А ошибка — это данные, пусть и ложные."
        },
        {
            "type": "jump",
            "next": 89
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Зависит от ситуации."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Все любят эту фразу."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Вздох.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Она почти всегда означает «я не знаю»."
        },
        {
            "type": "jump",
            "next": 89
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Сколько друзей нужно потерять."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Чтобы человек начал считать себя одиноким?"
        },
        {
            "type": "choice",
            "question": "Что ответить?",
            "options": [
                {
                    "text": "«Одного.»",
                    "next": 100,
                    "intellect": -1,
                    "respect": -1
                },
                {
                    "text": "«Всех.»",
                    "next": 104,
                    "intellect": 0,
                    "unconventional": 2
                },
                {
                    "text": "«Нет конкретного числа.»",
                    "next": 108,
                    "intellect": 2,
                    "respect": 1
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Одного."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Слишком сентиментально."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Потеря — это не бинарное состояние."
        },
        {
            "type": "jump",
            "next": 112
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Всех."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Абсолютно."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Но скучно."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Это тривиальный ответ."
        },
        {
            "type": "jump",
            "next": 112
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Нет конкретного числа."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Верно."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Одиночество — это не функция количества."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Это функция качества связей."
        },
        {
            "type": "jump",
            "next": 112
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Где мой друг?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Не знаю."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Но вероятность его отсутствия здесь равна единице."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Нормально ответить можешь?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Могу."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Не хочу."
        },
        {
            "type": "choice",
            "question": "Что сказать?",
            "options": [
                {
                    "text": "«Почему?»",
                    "next": 127,
                    "intellect": 1,
                    "respect": 1
                },
                {
                    "text": "«Ты меня бесишь.»",
                    "next": 131,
                    "intellect": -2,
                    "respect": -2
                },
                {
                    "text": "«Ты специально уходишь от ответа.»",
                    "next": 135,
                    "intellect": 2,
                    "unconventional": 2
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Почему?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Потому что ты спрашиваешь не «жив ли он»."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "А «где он»."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Значит, подсознательно уже выбрал ответ."
        },
        {
            "type": "jump",
            "next": 139
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Ты меня бесишь."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун делает пометку в блокноте.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Повышение голоса."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Эмоциональная реакция."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Результат пока неудовлетворительный."
        },
        {
            "type": "jump",
            "next": 139
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Ты намеренно уходишь от ответа."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун поднимает взгляд.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Верно."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Зачем?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Проверяю."
        },
        {
            "type": "jump",
            "next": 139
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Если бы тебе пришлось выбрать."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Узнать правду."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Или найти друга."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Что бы ты выбрал?"
        },
        {
            "type": "choice",
            "question": "Что выбрать?",
            "options": [
                {
                    "text": "«Найти друга.»",
                    "next": 150,
                    "intellect": -1,
                    "respect": -1
                },
                {
                    "text": "«Правду.»",
                    "next": 154,
                    "intellect": 2,
                    "respect": 2
                },
                {
                    "text": "«Зависит от правды.»",
                    "next": 158,
                    "unconventional": 3,
                    "respect": 1
                }
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Найти друга."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун делает пометку в блокноте.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_angry",
            "text": "Предсказуемо."
        },
        {
            "type": "jump",
            "next": 162
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Правду."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун впервые улыбается.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Опасный выбор."
        },
        {
            "type": "jump",
            "next": 162
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Зависит от правды."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Уклончиво."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Мне нравится."
        },
        {
            "type": "jump",
            "next": 162
        },
        {
            "type": "check_relationship",
            "conditions": {
                "anomaly": "unconventional >= 7",
                "prospect": "intellect >= 5",
                "noise": "default"
            },
            "branches": {
                "anomaly": 163,
                "prospect": 167,
                "noise": 171
            }
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Понятно."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Ты такой же."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Такой же кто?"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун долго молчит.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Поэтому Авель тебя и не отпустил бы."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Не отпустил бы куда?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Никуда.",
            "next_scene": "ending_anomaly"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Теперь понимаю."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что именно?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Почему брат решил тебя показать."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Он встаёт.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Есть потенциал."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Спасибо?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral_happy",
            "text": "Это не комплимент.",
            "next_scene": "ending_prospect"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Я закончил."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "И?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Слишком много шума."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Он открывает дверь.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Иди домой."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "А мой друг?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Если захочет — найдёт тебя сам.",
            "next_scene": "ending_noise"
        },
    ]

    def __init__(self, game, name):
        super().__init__(game, name, "assets/images/background_2.jpg")
        self.player_deception = False

        # Два отношения
        self.relationships[self.CLOWN_ID] = game.get_relationship(
            self.CLOWN_ID,
            custom_params={
                "intellect":      {"min": -10, "max": 10, "default": 0},
                "respect":        {"min": -10, "max": 10, "default": 0},
                "unconventional": {"min": 0,   "max": 10, "default": 0},
            }
        )
        self.relationships[self.ABEL_ID] = game.get_relationship(
            self.ABEL_ID,
            custom_params={
                "respect":   {"min": -10, "max": 10, "default": 5},
                "trust":     {"min": -10, "max": 10, "default": 5},
                "annoyance": {"min": 0,   "max": 10, "default": 0},
            }
        )

        # Фильтр диалогов — привязан к клоуну 2
        from algorithms.easy.dialogue_filter import DialogueFilter
        self.dialogue_filter = DialogueFilter(
            self.relationships[self.CLOWN_ID],
            game.player_tags
        )

        # Спрайт клоуна 2
        try:
            clown_states = {
                "clown_angry": "assets/images/clown_2/клоун 2.4.png",
                "clown_neutral_angry": "assets/images/clown_2/клоун 2.3.png",
                "clown_neutral_happy": "assets/images/clown_2/клоун 2.1.png",
                "clown_happy": "assets/images/clown_2/клоун 2.2.png",
            }
            clown = Character(
                "Клоун 2",
                "assets/images/clown_2/клоун 2.3.png",
                -420, 186,
                state_images=clown_states,
                default_state="clown_neutral_angry",
            )
            self.add_character(clown)
            self.clown_character = clown
            self.character_appeared = False
            self.appearance_timer = 0.0
            self.appearance_duration = 1.5
        except Exception as e:
            print(f"Ошибка загрузки спрайта персонажа: {e}")
            self.clown_character = None
            self.character_appeared = True

    # === Переопределения базового поведения ===

    def get_relationship(self, sprite_id=None):
        """По умолчанию — отношение с клоуном 2."""
        if sprite_id:
            return self.relationships.get(sprite_id)
        return self.relationships.get(self.CLOWN_ID)

    def _handle_check_relationship(self, current):
        """check_relationship в Place_2 всегда проверяет клоуна 2."""
        conditions = current["conditions"]
        branches = current["branches"]
        rel = self.get_relationship(self.CLOWN_ID)
        if not rel:
            return False

        for branch_name, condition in conditions.items():
            if rel.check(condition):
                self.current_dialogue = branches[branch_name]
                return True

        self.current_dialogue = list(branches.values())[-1]
        return True

    def _apply_line_effects(self, line):
        """В Place_2 нет эффектов в репликах."""
        pass

    def _on_choice_made(self, option):
        """Специфичная обработка выбора: клоун 2 + теги."""
        clown_before = self.relationships[self.CLOWN_ID].get_all().copy()
        tags_before = self.game.player_tags.get_all().copy()

        # Отношения с клоуном 2
        clown_changes = {}
        for param in ["intellect", "respect", "unconventional"]:
            if param in option:
                clown_changes[param] = option[param]
        if clown_changes:
            self.relationships[self.CLOWN_ID].modify(**clown_changes)

        # Теги игрока
        tag_changes = {}
        for tag in ["curious", "kind", "aggressive"]:
            if tag in option:
                tag_changes[tag] = option[tag]
        if tag_changes:
            self.game.player_tags.add(**tag_changes)

        # Запись в историю
        if hasattr(self.game, 'dialogue_history'):
            choice_question = ""
            all_options = []
            for i in range(self.current_dialogue, -1, -1):
                if self.dialogues[i].get("type") == "choice":
                    choice_question = self.dialogues[i].get("question", "")
                    all_options = self.dialogues[i].get("options", [])
                    break

            self.game.dialogue_history.record_choice(
                question=choice_question,
                selected_option=option,
                all_options=all_options,
                scene_name=self.name,
                effects={**clown_changes, **tag_changes}
            )

            clown_after = self.relationships[self.CLOWN_ID].get_all()
            if clown_before != clown_after:
                self.game.dialogue_history.record_relationship_change(
                    sprt_id=self.CLOWN_ID, before=clown_before, after=clown_after
                )

            tags_after = self.game.player_tags.get_all()
            if tags_before != tags_after:
                self.game.dialogue_history.record_tags_change(
                    before=tags_before, after=tags_after
                )

        print(f"[DEBUG] Clown2: {self.relationships[self.CLOWN_ID].get_all()} | "
              f"Tags: {self.game.player_tags.get_all()}")

        self._update_clown_emotion()

    # === Анимация и спрайты ===

    def update(self, dt):
        if self.clown_character and not self.character_appeared:
            self.appearance_timer += dt
            progress = min(self.appearance_timer / self.appearance_duration, 1.0)
            self.clown_character.x = -420 + progress * 400
            self.clown_character.opacity = int(130 + progress * 125)

            if progress >= 1.0:
                self.character_appeared = True
                self.clown_character.x = -20
                self.clown_character.opacity = 255

        super().update(dt)

    def _update_clown_emotion(self):
        """Обновляет эмоцию клоуна на основе intellect и unconventional."""
        if not self.clown_character:
            return

        intellect = self.relationships[self.CLOWN_ID].get("intellect")
        unconventional = self.relationships[self.CLOWN_ID].get("unconventional")

        if unconventional >= 7:
            self.clown_character.set_state("clown_happy")
        elif intellect >= 5:
            self.clown_character.set_state("clown_neutral_happy")
        elif intellect <= -3:
            self.clown_character.set_state("clown_angry")
        elif intellect < 0:
            self.clown_character.set_state("clown_neutral_angry")
        else:
            self.clown_character.set_state("clown_neutral_happy")

    def _sync_clown_sprite(self):
        """Синхронизация спрайта с текущей репликой."""
        if not self.clown_character:
            return
        current = self.get_current_dialogue()
        if not current:
            return

        if current.get("speaker") in ["Клоун", "Клоун 2"]:
            desired = current.get("sprite")
            if desired:
                self.clown_character.set_state(desired)
            else:
                self._update_clown_emotion()

    def draw(self, surface, mouse_pos=None):
        self._sync_clown_sprite()
        return super().draw(surface, mouse_pos)