from scenes.scene import Scene
from ui.button import Button


class HelpMenu(Scene):
    def __init__(self, game):
        super().__init__('pcst_kshmr_game/assets/images/background_0.jpg')
        self.game = game
        self.set_text("Справка - как играть?")
        
        # кнопка вернуться в меню
        back_btn = Button(
            300, 
            500, 
            200, 
            50, 
            "Вернуться", 
            (100, 100, 255), 
            (255, 255, 255), 
            lambda: game.change_scene("main_menu")
        )
        self.add_button(back_btn)
