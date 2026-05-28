from scenes.scene import Scene
from ui.button import Button
from scenes.menu.main_menu import MainMenu
from scenes.menu.settings_menu import SettingsMenu
from scenes.menu.load_menu import LoadMenu
from scenes.menu.help_menu import HelpMenu
from scenes.menu.about_menu import AboutMenu

class StartScene(Scene):
    def __init__(self, game):
        super().__init__('pcst_kshmr_game/assets/images/background_0.jpg')
        self.game = game
        self.set_text("тут какой-то текст начала. нажми 'далее' чтобы продолжить.")
        next_button = Button(350, 500, 100, 50, "далее", (0, 255, 0), (0, 0, 0), self.go_to_scene1)
        self.add_button(next_button)

    def go_to_scene1(self):
        self.game.change_scene("scene1")

class Scene1(Scene):
    def __init__(self, game):
        super().__init__('pcst_kshmr_game/assets/images/background_1.jpg')
        self.game = game
        self.set_text("тут уже текст по сцене")
        look_button = Button(200, 500, 100, 50, "выбор 1", (255, 0, 0), (0, 0, 0), self.look_around)
        exit_button = Button(500, 500, 100, 50, "выбор 2", (0, 0, 255), (255, 255, 255), self.exit_room)
        self.add_button(look_button)
        self.add_button(exit_button)

    def look_around(self):
        print("Выбрано: выбор 1")
        # логика перехода

    def exit_room(self):
        print("Выбрано: выбор 2")
        # логика перехода