import pygame
import sys
from scenes import StartScene, Scene1, MainMenu, SettingsMenu, LoadMenu, HelpMenu, AboutMenu, Place_0, Place_1, Place_2
from input_manager import InputManager

class Game:
    def __init__(self):
        pygame.init()
        
        self.LOGICAL_W, self.LOGICAL_H = 1280, 922

        self.window_width = self.LOGICAL_W
        self.window_height = self.LOGICAL_H
        self.fullscreen = False
        
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), 
            pygame.RESIZABLE
        )

        self.input_manager = InputManager()

        self.virtual_screen = pygame.Surface((self.LOGICAL_W, self.LOGICAL_H))

        pygame.display.set_caption("hello, clown")
        
        # тут будет иконка
        try:
            icon = pygame.image.load('assets/images/test_icon.jpg')
            pygame.display.set_icon(icon)
        except Exception as e:
            print(f"иконки пока нет: {e}")
        
        self.clock = pygame.time.Clock()
        self.scenes = {
            "start": StartScene(self),
            "scene1": Scene1(self),
            "main_menu": MainMenu(self),
            "settings_menu": SettingsMenu(self),
            "load_menu": LoadMenu(self),
            "help_menu": HelpMenu(self),
            "about_menu": AboutMenu(self),
            "0": Place_0(self),
            "1": Place_1(self),
            "2": Place_2(self),
        }
        self.current_scene = self.scenes["main_menu"]
        self.running = True
    
    def toggle_fullscreen(self):
        """переключение между полноэкранным и оконным режимом"""
        self.fullscreen = not self.fullscreen
        
        if self.fullscreen:
            display_info = pygame.display.Info()
            self.screen = pygame.display.set_mode(
                (display_info.current_w, display_info.current_h),
                pygame.FULLSCREEN
            )
        else:
            self.screen = pygame.display.set_mode(
                (self.window_width, self.window_height),
                pygame.RESIZABLE
            )
        
        self.window_width, self.window_height = self.screen.get_size()


    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            scene = self.scenes[scene_name]
            self.current_scene = scene(self) if callable(scene) else scene

    def _window_to_virtual_pos(self, pos):
        win_w, win_h = self.screen.get_size()
        scale = min(win_w / self.LOGICAL_W, win_h / self.LOGICAL_H)
        new_w = int(self.LOGICAL_W * scale)
        new_h = int(self.LOGICAL_H * scale)
        offset_x = (win_w - new_w) // 2
        offset_y = (win_h - new_h) // 2

        x, y = pos
        if x < offset_x or x > offset_x + new_w or y < offset_y or y > offset_y + new_h:
            return None

        return (
            int((x - offset_x) / scale),
            int((y - offset_y) / scale)
        )
    
    def _render_scaled(self):
        """отрисовка виртуального экрана с масштабированием на основной экран"""
        win_w, win_h = self.screen.get_size()
        
        scale = min(win_w / self.LOGICAL_W, win_h / self.LOGICAL_H)
        
        new_w = int(self.LOGICAL_W * scale)
        new_h = int(self.LOGICAL_H * scale)
        
        scaled = pygame.transform.scale(self.virtual_screen, (new_w, new_h))
        
        offset_x = (win_w - new_w) // 2
        offset_y = (win_h - new_h) // 2
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(scaled, (offset_x, offset_y))
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    if not self.fullscreen:
                        self.window_width = event.w
                        self.window_height = event.h
                        self.screen = pygame.display.set_mode(
                            (self.window_width, self.window_height),
                            pygame.RESIZABLE
                        )
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.toggle_fullscreen()
                    elif event.key == pygame.K_ESCAPE and self.fullscreen:
                        self.toggle_fullscreen()

                virtual_pos = None
                if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                    virtual_pos = self._window_to_virtual_pos(event.pos)
                    
                action = self.input_manager.process(event, mouse_click=virtual_pos)
                    
                self.current_scene.handle_event(event, mouse_pos=virtual_pos, action=action, dt=dt)

            real_mouse = pygame.mouse.get_pos()
            virtual_mouse = self._window_to_virtual_pos(real_mouse)
            self.current_scene.draw(self.virtual_screen, mouse_pos=virtual_mouse)
                
            self.current_scene.update(dt)
                
            self._render_scaled()

        pygame.quit()
        sys.exit()