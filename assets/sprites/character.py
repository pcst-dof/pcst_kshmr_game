import pygame


class Character:
    def __init__(self, name, image_path, x, y, state_images=None, default_state=None):
        self.name = name

        # визуал
        self.opacity = 255  # для прозрачности
        self.state = None
        self.original_images = {}  
        self.scaled_images = {}   
        self.image = None
        self.current_scale = 1.0

        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 0, 0)

        if state_images:
            for state_name, path in state_images.items():
                loaded = self._load_image(path)
                if loaded:
                    self.original_images[state_name] = loaded

            if default_state and default_state in self.original_images:
                self.set_state(default_state)
            elif self.original_images:
                self.state = next(iter(self.original_images))
                self.image = self.original_images[self.state]
        else:
            loaded = self._load_image(image_path)
            self.state = default_state or "default"
            if loaded:
                self.original_images[self.state] = loaded
                self.image = loaded

        self._update_rect()

    def _load_image(self, path):
        """Загружаем оригинал БЕЗ масштабирования"""
        try:
            image = pygame.image.load(path).convert_alpha()
            return image
        except Exception:
            if path.lower().endswith((".tiff", ".tif")):
                try:
                    from PIL import Image
                    pil_image = Image.open(path).convert("RGBA")
                    image = pygame.image.frombuffer(
                        pil_image.tobytes(), pil_image.size, pil_image.mode
                    )
                    return image.convert_alpha()
                except Exception:
                    placeholder = pygame.Surface((400, 550), pygame.SRCALPHA)
                    placeholder.fill((120, 0, 0, 180))
                    return placeholder
            placeholder = pygame.Surface((400, 550), pygame.SRCALPHA)
            placeholder.fill((120, 0, 0, 180))
            return placeholder

    def scale_to_screen(self, screen_w, screen_h, scale_factor=0.85):
        """Масштабируем все состояния персонажа под экран (вызывается один раз)"""
        if not self.original_images:
            return
        
        first_image = next(iter(self.original_images.values()))
        orig_w, orig_h = first_image.get_size()
        scale = min(screen_h * scale_factor / orig_h, screen_w * 0.6 / orig_w)
        
        if abs(scale - self.current_scale) < 0.01 and self.scaled_images:
            return
        
        self.current_scale = scale
        self.scaled_images = {}
        
        for state_name, orig_image in self.original_images.items():
            orig_w, orig_h = orig_image.get_size()
            new_w = int(orig_w * scale)
            new_h = int(orig_h * scale)
            
            if scale > 2.0:
                temp = pygame.transform.smoothscale(
                    orig_image, (orig_w * 2, orig_h * 2)
                )
                self.scaled_images[state_name] = pygame.transform.smoothscale(
                    temp, (new_w, new_h)
                )
            else:
                self.scaled_images[state_name] = pygame.transform.smoothscale(
                    orig_image, (new_w, new_h)
                )
        
        if self.state and self.state in self.scaled_images:
            self.image = self.scaled_images[self.state]
        self._update_rect()

    def set_state(self, state_name):
        if state_name in self.original_images:
            self.state = state_name
            if state_name in self.scaled_images:
                self.image = self.scaled_images[state_name]
            else:
                self.image = self.original_images[state_name]
            self._update_rect()
        else:
            print(f"Состояние персонажа не найдено: {state_name}")

    def _update_rect(self):
        if self.image:
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        else:
            self.rect = pygame.Rect(self.x, self.y, 0, 0)

    def draw(self, screen):
        if self.image:
            screen_w = screen.get_width()
            screen_h = screen.get_height()
            img_w = self.image.get_width()
            img_h = self.image.get_height()
                
            # Центрируем по X
            x = (screen_w - img_w) // 2
            # Центрируем по Y
            y = (screen_h - img_h) // 2
                
            # Применяем прозрачность
            image_with_alpha = self.image.copy()
            image_with_alpha.set_alpha(self.opacity)
            screen.blit(image_with_alpha, (x, y))
                
            # Обновляем rect с новыми координатами
            self.rect = image_with_alpha.get_rect(center=(screen_w // 2, screen_h // 2))