from scenes.scene import Scene
from ui.button import Button
from ui.actions.start_action import start_game
from ui.actions.load_action import load_game
from ui.actions.options_action import open_options
from ui.actions.help_action import open_help
from ui.actions.about_action import open_about
from ui.actions.exit_action import exit_game


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__('pcst_kshmr_game/assets/images/background_0.jpg')
        self.game = game
        self.set_text("Главное меню")
        
        # расстановка кнопок в колонну
        button_y_start = 150
        button_height = 50
        button_spacing = 80
        button_x = 300
        button_width = 200
        
        start_btn = Button(
            button_x, 
            button_y_start, 
            button_width, 
            button_height, 
            "Начать", 
            (0, 255, 0), 
            (0, 0, 0), 
            lambda: start_game(game)
        )
        
        load_btn = Button(
            button_x, 
            button_y_start + button_spacing, 
            button_width, 
            button_height, 
            "Загрузить", 
            (0, 200, 255), 
            (0, 0, 0), 
            lambda: load_game(game)
        )
        
        options_btn = Button(
            button_x, 
            button_y_start + button_spacing * 2, 
            button_width, 
            button_height, 
            "Настройки", 
            (255, 200, 0), 
            (0, 0, 0), 
            lambda: open_options(game)
        )
        
        help_btn = Button(
            button_x, 
            button_y_start + button_spacing * 3, 
            button_width, 
            button_height, 
            "Справка", 
            (255, 100, 100), 
            (0, 0, 0), 
            lambda: open_help(game)
        )
        
        about_btn = Button(
            button_x, 
            button_y_start + button_spacing * 4, 
            button_width, 
            button_height, 
            "О игре", 
            (150, 150, 255), 
            (0, 0, 0), 
            lambda: open_about(game)
        )
        
        exit_btn = Button(
            button_x, 
            button_y_start + button_spacing * 5, 
            button_width, 
            button_height, 
            "Выход", 
            (255, 0, 0), 
            (255, 255, 255), 
            lambda: exit_game(game)
        )
        
        self.add_button(start_btn)
        self.add_button(load_btn)
        self.add_button(options_btn)
        self.add_button(help_btn)
        self.add_button(about_btn)
        self.add_button(exit_btn)
