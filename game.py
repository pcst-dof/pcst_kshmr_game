import pygame
import sys
from scenes import StartScene, Scene1

class Game:
    def __init__(self):
        pygame.init()
        
        self.window_width = 800
        self.window_height = 600
        self.fullscreen = False
        
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), 
            pygame.RESIZABLE
        )
        
        pygame.display.set_caption("hello, clown")
        
        # тут будет иконка
        try:
            icon = pygame.image.load('pcst_kshmr_game/assets/images/test_icon.jpg')
            pygame.display.set_icon(icon)
        except Exception as e:
            print(f"иконки пока нет: {e}")
        
        self.clock = pygame.time.Clock()
        self.scenes = {
            "start": StartScene(self),
            "scene1": Scene1(self)
        }
        self.current_scene = self.scenes["start"]
        self.running = True
    
    def toggle_fullscreen(self):
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


    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def run(self):
        while self.running:
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

                self.current_scene.handle_event(event)

            self.current_scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()