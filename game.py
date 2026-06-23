import pygame
import sys
from scenes import StartScene, MainMenu, SettingsMenu, LoadMenu, HelpMenu, AboutMenu, Place_0, Place_1, Place_2, SaveMenu, PauseMenu
from input_manager import InputManager
from assets.sprites.character import Character
from algorithms.easy.scene_fsm import SceneFSM
from algorithms.medium.dialogue_history import DialogueHistory


class Game:
    def __init__(self):
        pygame.init()
        
        self.LOGICAL_W, self.LOGICAL_H = 1280, 922
        self.window_width = self.LOGICAL_W
        self.window_height = self.LOGICAL_H
        self.original_width = self.LOGICAL_W
        self.original_height = self.LOGICAL_H
        self.fullscreen = False
        
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height), 
            pygame.RESIZABLE | pygame.SCALED
        )

        self.input_manager = InputManager()
        self.virtual_screen = pygame.Surface((self.LOGICAL_W, self.LOGICAL_H))

        pygame.display.set_caption("hello, clown")
        
        try:
            icon = pygame.image.load('assets/images/test_icon.jpg')
            pygame.display.set_icon(icon)
        except Exception as e:
            print(f"иконки пока нет: {e}")
        
        self.clock = pygame.time.Clock()
        
        from algorithms.easy.player_tags import PlayerTags
        self.relationships = {}
        self.player_tags = PlayerTags()
        
        self.scene_fsm = SceneFSM(strict_mode=False)
        self._setup_scene_transitions()
        
        self.dialogue_history = DialogueHistory()
        
        self.scenes = {
            "start": StartScene(self),
            "main_menu": MainMenu(self),
            "settings_menu": SettingsMenu(self),
            "load_menu": LoadMenu(self),
            "save_menu": SaveMenu(self),  
            "help_menu": HelpMenu(self),
            "about_menu": AboutMenu(self),
            "pause_menu": PauseMenu(self),
            "0": Place_0(self, '0'),
            "1": Place_1(self, '1'),
            "2": Place_2(self, '2'),
        }

        self.current_scene = self.scenes["main_menu"]
        self.running = True

    def _setup_scene_transitions(self):
        fsm = self.scene_fsm
        
        fsm.add_transition("main_menu", "0")
        fsm.add_transition("main_menu", "settings_menu")
        fsm.add_transition("main_menu", "load_menu")
        fsm.add_transition("main_menu", "save_menu")
        fsm.add_transition("main_menu", "help_menu")
        fsm.add_transition("main_menu", "about_menu")
        fsm.add_transition("main_menu", "start")
        
        fsm.add_transition("start", "main_menu")
        
        fsm.add_transition("settings_menu", "main_menu")
        fsm.add_transition("load_menu", "main_menu")
        fsm.add_transition("save_menu", "main_menu")
        fsm.add_transition("help_menu", "main_menu")
        fsm.add_transition("about_menu", "main_menu")
        
        fsm.add_transition("0", "pause_menu")
        fsm.add_transition("1", "pause_menu")
        fsm.add_transition("2", "pause_menu")
        fsm.add_transition("pause_menu", "0")
        fsm.add_transition("pause_menu", "1")
        fsm.add_transition("pause_menu", "2")
        fsm.add_transition("pause_menu", "main_menu")
        fsm.add_transition("pause_menu", "settings_menu")
        fsm.add_transition("pause_menu", "save_menu")

        fsm.add_transition("settings_menu", "pause_menu")
        fsm.add_transition("save_menu", "pause_menu")
        fsm.add_transition("pause_menu", "save_menu")
        fsm.add_transition("save_menu", "pause_menu")
        
        fsm.add_transition("ending_stuck", "main_menu")

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        
        try:
            if self.fullscreen:
                display_info = pygame.display.Info()
                self.screen = pygame.display.set_mode(
                    (display_info.current_w, display_info.current_h),
                    pygame.FULLSCREEN
                )
            else:
                self.screen = pygame.display.set_mode(
                    (self.original_width, self.original_height),
                    pygame.RESIZABLE
                )
                self.window_width = self.original_width
                self.window_height = self.original_height
        except pygame.error as e:
            print(f"Ошибка переключения режима: {e}")
            self.fullscreen = not self.fullscreen

    def change_scene(self, scene_name):
        if scene_name not in self.scenes:
            print(f"[Game] Сцена '{scene_name}' не найдена")
            return
        
        current_name = None
        for name, scene in self.scenes.items():
            if scene is self.current_scene:
                current_name = name
                break
        
        if current_name and not self.scene_fsm.transition(current_name, scene_name):
            if self.scene_fsm.strict_mode:
                print(f"[Game] Переход {current_name} → {scene_name} запрещён FSM")
                return
        
        if current_name:
            self.dialogue_history.record_scene_change(current_name, scene_name)
        
        self.current_scene = self.scenes[scene_name]

    def get_relationship(self, sprt_id, custom_params=None):
        from algorithms.easy.relationship import Relationship
        
        if sprt_id not in self.relationships:
            self.relationships[sprt_id] = Relationship(sprt_id, custom_params)
        return self.relationships[sprt_id]

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

    def get_game_state(self):
        scene_name = None
        for name, scene in self.scenes.items():
            if scene is self.current_scene:
                scene_name = name
                current_dialogue = scene.current_dialogue
                break

        if scene_name is None:
            scene_name = getattr(self.current_scene, 'name', 'unknown')

        relationships_data = {
            sprt_id: rel.get_all() 
            for sprt_id, rel in self.relationships.items()
        }

        return {
            'current_scene': scene_name,
            'player_choices': getattr(self, 'player_choices', {}),
            'variables': getattr(self, 'variables', {}),
            'inventory': getattr(self, 'inventory', []),
            'flags': getattr(self, 'flags', {}),
            'relationships': relationships_data,
            'player_tags': self.player_tags.get_all(),
            'dialogue_history': self.dialogue_history.to_dict(),
            'current_dialogue': current_dialogue
        }

    def load_state(self, game_state):
        self.player_choices = game_state.get('player_choices', {})
        self.variables = game_state.get('variables', {})
        self.inventory = game_state.get('inventory', [])
        self.flags = game_state.get('flags', {})
        self._restore_relationships(game_state.get('relationships', {}))
        
        tags_data = game_state.get('player_tags', {})
        for tag_name, value in tags_data.items():
            if tag_name in self.player_tags.tags:
                self.player_tags.tags[tag_name]["value"] = value
        
        if 'dialogue_history' in game_state:
            self.dialogue_history = DialogueHistory.from_dict(game_state['dialogue_history'])

    def _restore_relationships(self, relationships_data):
        from algorithms.easy.relationship import Relationship
        
        self.relationships = {}
        for sprt_id, params in relationships_data.items():
            custom_params = {
                name: {"min": -10, "max": 10, "default": 0}
                for name in params
            }
            rel = Relationship(sprt_id, custom_params)
            
            for param_name, value in params.items():
                if param_name in rel.params:
                    rel.params[param_name]["value"] = value
            
            self.relationships[sprt_id] = rel

    def save_game(self, slot, screenshot=None):
        from utils.save_manager import SaveManager
        save_manager = SaveManager()
        game_state = self.get_game_state()
        save_manager.create_save(slot, game_state, screenshot)

    def _render_scaled(self):
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

                handled = self.current_scene.handle_event(
                    event,
                    mouse_pos=virtual_pos,
                    action=action,
                    dt=dt
                )

                if handled:
                    continue

            real_mouse = pygame.mouse.get_pos()
            virtual_mouse = self._window_to_virtual_pos(real_mouse)
            self.current_scene.draw(self.virtual_screen, mouse_pos=virtual_mouse)
                
            self.current_scene.update(dt)
                
            self._render_scaled()

        pygame.quit()
        sys.exit()