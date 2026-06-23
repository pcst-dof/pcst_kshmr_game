from scenes.base_dialogue_scene import BaseDialogueScene
from assets.sprites.character import Character


class Place_1(BaseDialogueScene):
    """Комната вкусного клоуна."""

    CLOWN_ID = "clown_1"
    ABEL_ID = "abel"
    NEXT_SCENE = "2"

    # Базовый класс создаст отношение по SPRITE_ID, но нам нужно два —
    # поэтому SPRITE_ID не задаём, а отношения создадим вручную в __init__
    SPRITE_ID = None
    RELATIONSHIP_PARAMS = {}

    DIALOGUES = [
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Ну и пылища тут."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "А чего ты ожидал от заброшенного здания?"
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Уж не знаю, но явно не такого количества пыли. Куда не глянь."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "*чихает*"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Тише ты.",
            "abel_respect": 1
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Чего тише-то? Кого ты боишься разбудить? Крыс?"
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Да тут, судя по количеству пыли, даже они не живут давно."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*На мгновение ГГ кажется, будто кто-то стоит около стены.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Однако стоит моргнуть два раза и уже никого не видно.*"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Никого.*"
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Ты чего завис?"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Да так, показалось."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Ну-ну."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Герои аккуратно исследуют комнату.*"
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Слушай, а если тут реально кто-то живет?"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Думаю, что мы бы заметили что-нибудь подозрительное."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Тоже верно, не думаю, что это бы прошло зря..."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Подожди... Мне кажется, или стало слишком тихо?"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "ГГ?"
        },
        {
            "type": "line",
            "speaker": "???",
            "text": "Бу.",
            "sprite": "clown_happy"
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "ТВОЮ МАТЬ!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "О, этот испугался."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "А вот ты не очень."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Ты кто вообще? В курсе, что так пугать людей..."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Бла-бла-бла. Как грубо."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Твой?"
        },
        {
            "type": "choice",
            "question": "Как ответить Клоуну?",
            "options": [
                {
                    "text": "«Вообще-то он сам по себе.»",
                    "next": 30,
                    "interest": 2,
                    "kind": 5,
                    "abel_trust": -1
                },
                {
                    "text": "«Да, мой друг.»",
                    "next": 38,
                    "interest": 0,
                    "kind": 3,
                    "abel_trust": 1
                },
                {
                    "text": "«А ты кто?»",
                    "next": 48,
                    "interest": 3,
                    "curious": 5,
                    "abel_respect": 1
                },
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Вообще-то он сам по себе."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Правда?"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Наклоняет голову.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "А я уж подумал, что вы пришли комплектом."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Да пошёл ты.",
            "abel_respect": -1
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Нет, спасибо."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*И снова смотрит только на ГГ.*"
        },
        {
            "type": "jump",
            "next": 68
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Да, мой друг."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун некоторое время молчит.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Жаль."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Ничего."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Просто вы вдвоём занимаете слишком много места."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Мы буквально стоим на месте."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Вот именно."
        },
        {
            "type": "jump",
            "next": 68
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "А ты кто?"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун аж замирает.*"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Потом широко улыбается.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "О."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Наконец-то правильный вопрос."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Подходит чуть ближе. Слишком близко.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "А как думаешь?"
        },
        {
            "type": "choice",
            "question": "Что ответить?",
            "options": [
                {
                    "text": "«Местный псих.»",
                    "next": 56,
                    "interest": 0,
                    "aggressive": 3
                },
                {
                    "text": "«Работник цирка?»",
                    "next": 60,
                    "interest": 0,
                    "curious": 2
                },
                {
                    "text": "«Понятия не имею.»",
                    "next": 64,
                    "interest": 0,
                    "kind": 2
                },
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Местный псих."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун смеётся. Искренне. Первый раз за сцену.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Хорошо начал."
        },
        {
            "type": "jump",
            "next": 68
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Работник цирка?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Когда-то был."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Пауза.*"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Наверное."
        },
        {
            "type": "jump",
            "next": 68
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Понятия не имею."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "И это тоже хороший ответ."
        },
        {
            "type": "jump",
            "next": 68
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Так вот, на чем мы остановились..."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Может кто-нибудь объяснит что тут происходит?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Он всегда столько говорит?"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Я вообще-то здесь стою!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "И правда. Думаю, пора это исправить."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "О чем ты.. Что ты?!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Знаешь."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Мне кажется, мы друг другу мешаем."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Я не о тебе, мой сладкий."
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун злобно смотрит на Авеля.*",
            "sprite": "clown_angry"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Я говорю о нем."
        },
        {
            "type": "line",
            "speaker": "Авель",
            "text": "Слушай, я сейчас тебе..."
        },
        {
            "type": "line",
            "speaker": "???",
            "text": "*Резкий звук захлопнувшей двери.*"
        },
        {
            "type": "line",
            "speaker": "???",
            "text": "*Тишина*"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "..."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Авель?"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Где он?!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Ты действительно хочешь сейчас говорить о нём?"
        },
        {
            "type": "choice",
            "question": "Что сказать?",
            "options": [
                {
                    "text": "«Да. Где мой друг?»",
                    "next": 90,
                    "interest": -2,
                    "kind": 5,
                    "abel_trust": 2
                },
                {
                    "text": "«Что ты с ним сделал?»",
                    "next": 94,
                    "interest": 1,
                    "aggressive": 3,
                    "abel_respect": 1
                },
                {
                    "text": "«Как ты это сделал?»",
                    "next": 98,
                    "interest": 3,
                    "curious": 7,
                    "abel_trust": -2
                },
                {
                    "text": "«Мне всё равно. Где выход?»",
                    "next": 103,
                    "condition": "aggressive >= 10",
                    "interest": -5,
                    "aggressive": 3,
                    "abel_trust": -3
                },
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Да. Где мой друг?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Опять про него?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Ладно. Ушёл. Не вернётся. Доволен?"
        },
        {
            "type": "jump",
            "next": 103
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Что ты с ним сделал?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Сделал? Ничего особенного. Просто... убрал с глаз долой."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Теперь мы можем говорить нормально."
        },
        {
            "type": "jump",
            "next": 103
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Как ты это сделал?"
        },
        {
            "type": "line",
            "speaker": "***",
            "text": "*Клоун буквально расцветает.*",
            "sprite": "clown_happy"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "А вот это уже намного интереснее."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Магия, дружок. Чистая магия."
        },
        {
            "type": "jump",
            "next": 103
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Знаешь, ты мне нравишься."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Ты не такой, как другие. В тебе есть... искра."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Хочешь, покажу тебе кое-что особенное?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "У меня тут есть секретная комната. Только для избранных."
        },
        {
            "type": "choice",
            "question": "Что ответить?",
            "options": [
                {
                    "text": "«Конечно! Покажи!»",
                    "next": 108,
                    "interest": 3,
                    "obsession": 1,
                    "curious": 5
                },
                {
                    "text": "«Нет, спасибо. Мне лучше идти.»",
                    "next": 112,
                    "interest": -3,
                    "obsession": 2,
                    "aggressive": 2
                },
                {
                    "text": "«...Ладно, покажи. Но потом я ухожу.»",
                    "next": 116,
                    "interest": 1,
                    "obsession": 0,
                    "deception": True,
                    "curious": 3
                },
                {
                    "text": "«А что, если я сам покажу тебе кое-что?»",
                    "next": 108,
                    "condition": "curious >= 15",
                    "interest": 5,
                    "curious": 5
                },
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Конечно! Покажи!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "О, чудесно!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Ты не пожалеешь! Это будет... незабываемо!"
        },
        {
            "type": "jump",
            "next": 120
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Нет, спасибо. Мне лучше идти."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Уходишь? Так быстро?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Но мы только начали! Ты разочаровываешь меня, дружок."
        },
        {
            "type": "jump",
            "next": 120
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "...Ладно, покажи. Но потом я ухожу."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Условию? Ха!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Хорошо, хорошо. Покажу, а там посмотрим. Идем!"
        },
        {
            "type": "jump",
            "next": 120
        },
        {
            "type": "line",
            "speaker": "Narrator",
            "text": "Клоун ведет тебя через темный коридор. Стены здесь покрыты странными символами."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Вот она! Моя гордость!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Здесь я показываю свои лучшие фокусы. Только для самых особых гостей."
        },
        {
            "type": "line",
            "speaker": "Narrator",
            "text": "В центре комнаты стоит стул с ремнями. Рядом — странные инструменты."
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Это... это что за фокусы?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "О, это мой главный трюк!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Доброволец садится в стул, а я... делаю его вечным! Навсегда частью шоу!"
        },
        {
            "type": "choice",
            "question": "Что делать?",
            "options": [
                {
                    "text": "«Ты сумасшедший! Я не сяду в этот стул!»",
                    "next": 128,
                    "interest": -2,
                    "obsession": 3,
                    "resistance": 2,
                    "aggressive": 5
                },
                {
                    "text": "«...Интересно. А что если я сяду сам?»",
                    "next": 132,
                    "interest": 4,
                    "obsession": 2,
                    "curious": 8
                },
                {
                    "text": "«Круто! А можно я посмотрю со стороны?»",
                    "next": 136,
                    "interest": 0,
                    "obsession": 1,
                    "kind": 3
                },
            ]
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Ты сумасшедший! Я не сяду в этот стул!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Сумасшедший? Я — АРТИСТ!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Ты оскорбляешь мое искусство!"
        },
        {
            "type": "jump",
            "next": 140
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "...Интересно. А что если я сяду сам?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Сам? О, какой восторг!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Какой энтузиазм! Ты действительно особенный!"
        },
        {
            "type": "jump",
            "next": 147
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Круто! А можно я посмотрю со стороны?"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Со стороны? Но это не так интересно!"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Настоящее шоу требует участия!"
        },
        {
            "type": "jump",
            "next": 140
        },
        {
            "type": "check_relationship",
            "conditions": {
                "high": "interest >= 5",
                "medium": "interest >= 0",
                "low": "interest < 0",
            },
            "branches": {
                "high": 141,
                "medium": 143,
                "low": 145,
            }
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Знаешь что? Ты слишком интересен, чтобы уходить."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Ты останешься здесь. Навсегда.",
            "next_scene": "ending_stuck"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Ладно, ладно. Ты мне нравишься, но не настолько."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_neutral",
            "text": "Иди к моему брату. Пусть он решит, что с тобой делать.",
            "next_scene": "2"
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Знаешь что? Ты скучный."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_angry",
            "text": "Иди к моему брату. Пусть он сам разбирается с такими, как ты.",
            "next_scene": "2"
        },
        {
            "type": "line",
            "speaker": "Narrator",
            "text": "Ты садишься в стул. Клоун затягивает ремни."
        },
        {
            "type": "line",
            "speaker": "Клоун",
            "sprite": "clown_happy",
            "text": "Спасибо, дружок! Ты будешь лучшим экспонатом в моей коллекции!"
        },
        {
            "type": "line",
            "speaker": "ГГ",
            "text": "Подожди, я передумал! Отпусти!",
            "next_scene": "ending_stuck"
        },
    ]

    def __init__(self, game, name):
        super().__init__(game, name, "assets/images/background_1.jpg")
        self.player_deception = False

        # Два отношения — создаём вручную (базовый класс не знает про ABEL_ID)
        self.relationships[self.CLOWN_ID] = game.get_relationship(
            self.CLOWN_ID,
            custom_params={
                "interest":   {"min": -10, "max": 10, "default": 0},
                "obsession":  {"min": 0,   "max": 10, "default": 0},
                "resistance": {"min": 0,   "max": 5,  "default": 0},
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

        # Фильтр диалогов — привязан к клоуну
        from algorithms.easy.dialogue_filter import DialogueFilter
        self.dialogue_filter = DialogueFilter(
            self.relationships[self.CLOWN_ID],
            game.player_tags
        )

        # Спрайт клоуна
        try:
            friend_states = {
                "clown_angry": "assets/images/clown_1/клоун 1.1.png",
                "clown_neutral": "assets/images/clown_1/клоун 1.2.png",
                "clown_happy": "assets/images/clown_1/клоун 1.3.png",
            }
            friend = Character(
                "Клоун",
                "assets/images/clown_1/клоун 1.2.png",
                -420, 186,
                state_images=friend_states,
                default_state="clown_neutral",
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

    # === Переопределения базового поведения ===

    def get_relationship(self, sprite_id=None):
        """По умолчанию — отношение с клоуном (для check_relationship и фильтра)."""
        if sprite_id:
            return self.relationships.get(sprite_id)
        return self.relationships.get(self.CLOWN_ID)

    def _handle_check_relationship(self, current):
        """check_relationship в Place_1 всегда проверяет клоуна."""
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
        """Эффекты в репликах: abel_respect, abel_trust, abel_annoyance."""
        abel_changes = {}
        for param in ["respect", "trust", "annoyance"]:
            key = f"abel_{param}"
            if key in line:
                abel_changes[param] = line[key]

        if abel_changes:
            self.relationships[self.ABEL_ID].modify(**abel_changes)

    def _on_choice_made(self, option):
        """Специфичная обработка выбора: клоун + Авель + теги."""
        clown_before = self.relationships[self.CLOWN_ID].get_all().copy()
        abel_before = self.relationships[self.ABEL_ID].get_all().copy()
        tags_before = self.game.player_tags.get_all().copy()

        # Отношения с клоуном
        clown_changes = {}
        for param in ["interest", "obsession", "resistance"]:
            if param in option:
                clown_changes[param] = option[param]
        if clown_changes:
            self.relationships[self.CLOWN_ID].modify(**clown_changes)

        # Отношения с Авелем (в опциях с префиксом abel_)
        abel_changes = {}
        for param in ["abel_respect", "abel_trust", "abel_annoyance"]:
            if param in option:
                abel_changes[param.replace("abel_", "")] = option[param]
        if abel_changes:
            self.relationships[self.ABEL_ID].modify(**abel_changes)

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
                effects={**clown_changes, **abel_changes, **tag_changes}
            )

            clown_after = self.relationships[self.CLOWN_ID].get_all()
            if clown_before != clown_after:
                self.game.dialogue_history.record_relationship_change(
                    sprt_id=self.CLOWN_ID, before=clown_before, after=clown_after
                )

            abel_after = self.relationships[self.ABEL_ID].get_all()
            if abel_before != abel_after:
                self.game.dialogue_history.record_relationship_change(
                    sprt_id=self.ABEL_ID, before=abel_before, after=abel_after
                )

            tags_after = self.game.player_tags.get_all()
            if tags_before != tags_after:
                self.game.dialogue_history.record_tags_change(
                    before=tags_before, after=tags_after
                )

        print(f"[DEBUG] Clown: {self.relationships[self.CLOWN_ID].get_all()} | "
              f"Abel: {self.relationships[self.ABEL_ID].get_all()} | "
              f"Tags: {self.game.player_tags.get_all()}")

        if option.get("deception"):
            self.player_deception = True

        self._update_clown_emotion()

    # === Анимация и спрайты ===

    def update(self, dt):
        if self.friend_character and not self.character_appeared:
            self.appearance_timer += dt
            progress = min(self.appearance_timer / self.appearance_duration, 1.0)
            self.friend_character.x = -420 + progress * 400
            self.friend_character.opacity = int(130 + progress * 125)

            if progress >= 1.0:
                self.character_appeared = True
                self.friend_character.x = -20
                self.friend_character.opacity = 255

        super().update(dt)

    def _update_clown_emotion(self):
        if not self.friend_character:
            return
        interest = self.relationships[self.CLOWN_ID].get("interest")
        if interest >= 5:
            self.friend_character.set_state("clown_happy")
        elif interest >= 0:
            self.friend_character.set_state("clown_neutral")
        else:
            self.friend_character.set_state("clown_angry")

    def _sync_friend_sprite(self):
        if not self.friend_character:
            return
        current = self.get_current_dialogue()
        if not current:
            return

        if current.get("speaker") in ["Клоун", "Хирото"]:
            desired = current.get("sprite")
            if desired:
                self.friend_character.set_state(desired)
            else:
                self._update_clown_emotion()

    def draw(self, surface, mouse_pos=None):
        self._sync_friend_sprite()
        return super().draw(surface, mouse_pos)