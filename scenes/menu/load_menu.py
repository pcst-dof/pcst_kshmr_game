import os

from scenes.menu.main_menu import BASE_DIR
from scenes.scene import Scene
from ui.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MY_FONT_PATH = os.path.join(BASE_DIR, 'fronts', 'Greengoth_Exp_SHA_0.otf')
MY_FONT_SIZE = 40


class LoadMenu(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.png')
        self.game = game
        self.set_text("Сохранить игру")
        
        # кнопка вернуться в меню внизу по центру
        button_width = 260
        button_height = 56
        button_x = (self.game.LOGICAL_W - button_width) // 2
        button_y = self.game.LOGICAL_H - 130

        back_btn = Button(
            button_x,
            button_y,
            button_width,
            button_height,
            "Вернуться",
            (100, 100, 255),
            (255, 255, 255),
            lambda: game.change_scene("main_menu"),
            font_path=MY_FONT_PATH,
            font_size=MY_FONT_SIZE 
        )
        self.add_button(back_btn)
