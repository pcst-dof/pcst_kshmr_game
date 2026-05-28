import pygame
from scenes.scene import Scene
from ui.button import Button

class StartScene(Scene):
    def __init__(self, game):
        super().__init__(game, 'assets/images/background_0.jpg')
        self.set_text("выберите действие")
        menu_items = [
            ("Start", self.go_to_scene1),
            ("Load", self.load_game),
            ("Options", self.open_options),
            ("Help", self.show_help),
            ("About", self.show_about),
            ("Quit", self.quit_game),
        ]
        btn_width = 200
        btn_height = 40
        gap = 18
        total_height = len(menu_items) * btn_height + (len(menu_items) - 1) * gap
        btn_x = (self.game.LOGICAL_W - btn_width) // 2
        btn_y = (self.game.LOGICAL_H - total_height) // 2

        for text, action in menu_items:
            btn = Button(
                btn_x,
                btn_y,
                btn_width,
                btn_height,
                text,
                (200, 200, 200),
                (240, 240, 245),
                action,
                hover_color=(255, 255, 255),
                font_size=28,
            )
            self.add_button(btn)
            btn_y += btn_height + gap

    def draw(self, surface):
        if self.background:
            surface.blit(self.background, (0, 0))
        else:
            surface.fill((0, 0, 0))

        overlay = pygame.Surface((self.game.LOGICAL_W, self.game.LOGICAL_H), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 90))
        surface.blit(overlay, (0, 0))

        if self.text:
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            surface.blit(text_surface, (60, 110))

        for button in self.buttons:
            button.draw(surface)

    def go_to_scene1(self):
        self.game.change_scene("scene1")

    def load_game(self):
        print("загрузка сохранения...")

    def open_options(self):
        print("настройки...")

    def show_help(self):
        print("помощь...")

    def show_about(self):
        print("об игре...")

    def quit_game(self):
        self.game.running = False

class Scene1(Scene):
    def __init__(self, game):
        super().__init__(game, 'assets/images/background_1.jpg')
        self.set_text("тут уже текст по сцене")
        look_button = Button(200, 500, 100, 50, "выбор 1", (255, 0, 0), (0, 0, 0), self.look_around)
        exit_button = Button(500, 500, 100, 50, "выбор 2", (0, 0, 255), (255, 255, 255), self.exit_room)
        self.add_button(look_button)
        self.add_button(exit_button)

    def look_around(self):
        print("выбрано: выбор 1")
        # логика перехода

    def exit_room(self):
        print("выбрано: выбор 2")
        # логика перехода