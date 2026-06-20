import sys

def start_game(game):
    """переход в начало игры"""
    # Переключаем сначала на сцену ввода имени, затем StartScene сама перейдёт в игру
    game.change_scene("start")


def open_options(game):
    """переход на экран настроек"""
    game.change_scene("settings_menu")


def load_game(game):
    """переход на экран загрузки игры"""
    game.change_scene("load_menu")


def open_help(game):
    """переход на экран справки"""
    game.change_scene("help_menu")


def exit_game(game):
    """выход из игры"""
    game.running = False
    sys.exit()


def open_about(game):
    """переход на экран информации об игре"""
    game.change_scene("about_menu")
