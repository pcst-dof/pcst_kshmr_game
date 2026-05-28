import pygame
import sys
from pathlib import Path
from scenes import StartScene, Scene1

class Game:
    def __init__(self):
        pygame.init()
        
        # логическое разрешение игры
        self.LOGICAL_W, self.LOGICAL_H = 800, 600

        # начальный размер окна
        self.window_width = self.LOGICAL_W
        self.window_height = self.LOGICAL_H
        self.fullscreen = False
        
        # флаг для масштабирования при изменении размера окна
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), 
            pygame.RESIZABLE
        )
        
        # виртуальный экран для отрисовки с логическим разрешением
        self.virtual_screen = pygame.Surface((self.LOGICAL_W, self.LOGICAL_H))

        pygame.display.set_caption("hello, clown")
        
        # тут будет иконка
        try:
            icon_path = Path(__file__).resolve().parent / "assets" / "images" / "test_icon.jpg"
            icon = pygame.image.load(str(icon_path))
            pygame.display.set_icon(icon)
        except Exception as e:
            print(f"иконки пока нет: {e}")
        
        self.clock = pygame.time.Clock()
        self.fade_alpha = 255
        self.scenes = {
            "start": StartScene(self),
            "scene1": Scene1(self)
        }
        self.current_scene = self.scenes["start"]
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
        
        # обновляем размеры окна для масштабирования
        self.window_width, self.window_height = self.screen.get_size()


    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]
    
    def _render_scaled(self):
        """отрисовка виртуального экрана с масштабированием на основной экран"""
        win_w, win_h = self.screen.get_size()
        
        # вычисляем коэфф масштабирования, сохраняя пропорции
        scale = min(win_w / self.LOGICAL_W, win_h / self.LOGICAL_H)
        
        # новые размеры отрисовки виртуального экрана
        new_w = int(self.LOGICAL_W * scale)
        new_h = int(self.LOGICAL_H * scale)
        
        # масштабируем виртуальный экран до новых размеров
        scaled = pygame.transform.scale(self.virtual_screen, (new_w, new_h))
        
        # отступы для центрирования отрисовки
        offset_x = (win_w - new_w) // 2
        offset_y = (win_h - new_h) // 2
        
        self.screen.fill((0, 0, 0))  # черный фон за пределами отрисовки
        self.screen.blit(scaled, (offset_x, offset_y))
        pygame.display.flip()

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

            # отрисовка на виртуальный экран
            self.current_scene.draw(self.virtual_screen)
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.LOGICAL_W, self.LOGICAL_H))
                fade_surface.set_alpha(self.fade_alpha)
                fade_surface.fill((0, 0, 0))
                self.virtual_screen.blit(fade_surface, (0, 0))
                self.fade_alpha = max(0, self.fade_alpha - int(self.clock.get_time() * 0.4))
            self._render_scaled()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()