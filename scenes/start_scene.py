import pygame
from scenes.scene import Scene
from ui.button import Button


class StartScene(Scene):
    def __init__(self, game):
        super().__init__('assets/images/background_0.jpg')
        self.game = game
        self.set_text("What's your name?")

        self.input_text = ""
        self.input_active = True
        self.box_w, self.box_h = 500, 60
        self.box_x = (self.game.LOGICAL_W - self.box_w) // 2
        self.box_y = 340
        self.box_rect = pygame.Rect(self.box_x, self.box_y, self.box_w, self.box_h)
        self.cursor_visible = True
        self.show_bottom_menu = False
        self.last_cursor_toggle = pygame.time.get_ticks()

        btn_w, btn_h = 220, 70
        btn_x = (self.game.LOGICAL_W - btn_w) // 2
        btn_y = 420
        next_button = Button(btn_x, btn_y, btn_w, btn_h, "Next >", (180, 180, 180), (200, 200, 200), self.go_to_scene1, font_size=48)
        self.add_button(next_button)

    def draw(self, screen, mouse_pos=None):
        super().draw(screen, mouse_pos)

        title_font = pygame.font.SysFont(None, 36)
        question_surf = title_font.render("What's your name?", True, (230, 230, 230))
        qx = (self.game.LOGICAL_W - question_surf.get_width()) // 2
        qy = 300
        screen.blit(question_surf, (qx, qy))

        pygame.draw.rect(screen, (20, 20, 20), self.box_rect)
        pygame.draw.rect(screen, (180, 180, 180), self.box_rect, 2, border_radius=8)

        display_text = self.input_text if self.input_text else "Enter your name..."
        txt_surf = self.font.render(display_text, True, (200, 200, 200))
        screen.blit(txt_surf, (self.box_x + 16, self.box_y + (self.box_h - txt_surf.get_height()) // 2))

        now = pygame.time.get_ticks()
        if now - self.last_cursor_toggle > 500:
            self.cursor_visible = not self.cursor_visible
            self.last_cursor_toggle = now

        if self.input_active and self.cursor_visible:
            cursor_x = self.box_x + 16 + txt_surf.get_width() + 2
            cursor_y = self.box_y + 12
            pygame.draw.rect(screen, (220, 220, 220), (cursor_x, cursor_y, 2, self.box_h - 24))

    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = mouse_pos if mouse_pos is not None else event.pos
            if click_pos is not None and self.box_rect.collidepoint(click_pos):
                self.input_active = True
                return True
            if click_pos is not None and not self.box_rect.collidepoint(click_pos):
                for button in self.buttons:
                    if button.is_clicked(click_pos):
                        if button.action:
                            button.action()
                        return True

        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
                return True
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.go_to_scene1()
                return True
            else:
                char = event.unicode
                if char.isprintable() and len(self.input_text) < 30:
                    self.input_text += char
                    return True

        return super().handle_event(event, mouse_pos=mouse_pos, action=action, dt=dt)

    def go_to_scene1(self):
        name = self.input_text.strip() or "Player"
        self.game.player_name = name
        self.game.change_scene("0")