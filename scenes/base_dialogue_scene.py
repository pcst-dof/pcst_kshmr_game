import pygame
from scenes.scene import Scene
from algorithms.easy.dialogue_filter import DialogueFilter
from algorithms.medium.dialogue_tree import DialogueTree


class BaseDialogueScene(Scene):
    """Базовый класс для сцен с диалогами"""
    
    SPRITE_ID = None
    DIALOGUES = []
    RELATIONSHIP_PARAMS = {}
    NEXT_SCENE = None
    
    def __init__(self, game, name, background_path):
        super().__init__(background_path, name)
        self.game = game
        self.choice_active = False
        self.show_bottom_menu = True
        self.selected_choice = 0
        
        self.relationships = {}
        if self.SPRITE_ID and self.RELATIONSHIP_PARAMS:
            self.relationships[self.SPRITE_ID] = game.get_relationship(
                self.SPRITE_ID,
                custom_params=self.RELATIONSHIP_PARAMS
            )
        
        primary_rel = list(self.relationships.values())[0] if self.relationships else None
        self.dialogue_filter = DialogueFilter(primary_rel, game.player_tags) if primary_rel else None
        
        self.dialogues = self.DIALOGUES
        self.current_dialogue = 0
        self.auto_advance_timer = 0
        self._last_recorded_index = None
        
        self.dialogue_tree = DialogueTree()
        self.dialogue_tree.build_from_dialogues(self.dialogues)
        
        stats = self.dialogue_tree.get_stats()
        print(f"[{self.__class__.__name__}] Дерево диалогов построено:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    
    def get_relationship(self, sprite_id=None):
        if sprite_id:
            return self.relationships.get(sprite_id)
        return list(self.relationships.values())[0] if self.relationships else None
    
    def _record_current_dialogue(self):
        if not hasattr(self.game, 'dialogue_history'):
            return
        
        current = self.get_current_dialogue()
        if not current:
            return
        
        if current.get("type") in ("jump", "check_relationship"):
            return
        
        if self._last_recorded_index == self.current_dialogue:
            return
        
        self._last_recorded_index = self.current_dialogue
        
        if current.get("type") == "line":
            self.game.dialogue_history.record_line(
                speaker=current.get("speaker", ""),
                text=current.get("text", ""),
                scene_name=self.name
            )
        elif current.get("type") == "choice":
            available = self._get_available_choices()
            self.game.dialogue_history.record_choice_prompt(
                question=current.get("question", ""),
                options=available,
                scene_name=self.name
            )
    
    def _get_available_choices(self):
        current = self.get_current_dialogue()
        if not current or current.get("type") != "choice":
            return []
        if self.dialogue_filter:
            return self.dialogue_filter.filter_choices(current["options"])
        return current["options"]
    
    def get_current_dialogue(self):
        while 0 <= self.current_dialogue < len(self.dialogues):
            current = self.dialogues[self.current_dialogue]
            
            if current.get("type") == "jump":
                self.current_dialogue = current["next"]
                continue
            
            if current.get("type") == "check_relationship":
                if not self._handle_check_relationship(current):
                    break
                continue
            
            return current
        
        return None
    
    def _handle_check_relationship(self, current):
        conditions = current["conditions"]
        branches = current["branches"]
        
        rel = self.get_relationship()
        if not rel:
            return False
        
        for branch_name, condition in conditions.items():
            if rel.check(condition):
                self.current_dialogue = branches[branch_name]
                return True
        
        self.current_dialogue = list(branches.values())[-1]
        return True
    
    def handle_event(self, event, mouse_pos=None, action=None, dt=0):
        current = self.get_current_dialogue()
        if not current:
            return super().handle_event(event, mouse_pos, action, dt)
        
        self._record_current_dialogue()
        
        # Клавиатурное управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current["type"] == "line":
                self._apply_line_effects(current)
                return self._advance_dialogue()
            
            if current["type"] == "choice":
                available = self._get_available_choices()
                if event.key == pygame.K_UP:
                    self.selected_choice = max(0, self.selected_choice - 1)
                    return True
                elif event.key == pygame.K_DOWN:
                    self.selected_choice = min(len(available) - 1, self.selected_choice + 1)
                    return True
                elif event.key == pygame.K_RETURN:
                    if available:
                        option = available[self.selected_choice]
                        self.current_dialogue = option["next"]
                        self._on_choice_made(option)
                        self.selected_choice = 0
                    return True
        
        # Обработка действий от InputManager
        if not super().handle_event(event, mouse_pos, action, dt):
            if action == 'advance':
                if current["type"] == "line":
                    self._apply_line_effects(current)
                    return self._advance_dialogue()
                elif current["type"] == "choice":
                    available = self._get_available_choices()
                    if available:
                        option = available[self.selected_choice]
                        self.current_dialogue = option["next"]
                        self._on_choice_made(option)
                        self.selected_choice = 0
                    return True
            
            # === Обработка СКМ ===
            if action == 'toggle_ui':
                self.show_bottom_menu = not self.show_bottom_menu
                return True
            
            # === Обработка колёсика вверх ===
            if action == 'dialogue_back':
                if self.history:
                    self.current_dialogue = self.history.pop()
                    return True
                return False
            
            # === Обработка колёсика вниз ===
            if action == 'dialogue_forward':
                return self._advance_dialogue()
            
            if current["type"] == "choice":
                available = self._get_available_choices()
                if action == 'nav_up':
                    self.selected_choice = max(0, self.selected_choice - 1)
                    return True
                if action == 'nav_down':
                    self.selected_choice = min(len(available) - 1, self.selected_choice + 1)
                    return True
            
            # === ПКМ ===
            if action == 'menu':
                pause_menu = self.game.scenes.get('pause_menu')
                if pause_menu:
                    pause_menu.previous_scene = self.name
                self.game.change_scene('pause_menu')
                return True
            
            return False
        return True
    
    def _advance_dialogue(self):
        current = self.get_current_dialogue()
        if not current:
            return False
        
        if "next_scene" in current:
            self.game.change_scene(current["next_scene"])
            return True
        if "next" in current:
            self.current_dialogue = current["next"]
            return True
        self.next_dialogue()
        return True
    
    def update(self, dt):
        if self.game.input_manager.is_skipping():
            self.auto_advance_timer += dt
            if self.auto_advance_timer >= 0.05:
                self.auto_advance_timer = 0
                current = self.get_current_dialogue()
                if current and current["type"] == "line":
                    self._apply_line_effects(current)
                    if "next_scene" in current:
                        self.game.change_scene(current["next_scene"])
                        return
                    if "next" in current:
                        self.current_dialogue = current["next"]
                        return
                    self.next_dialogue()
        else:
            super().update(dt)
    
    def next_dialogue(self):
        current = self.get_current_dialogue()
        if current and "next_scene" in current:
            self.game.change_scene(current["next_scene"])
            return
        
        self.history.append(self.current_dialogue)
        
        if self.current_dialogue < len(self.dialogues) - 1:
            self.current_dialogue += 1
            current = self.get_current_dialogue()
            
            if self.skip_mode and current and current.get("type") == "choice":
                self.skip_mode = False
        else:
            if self.NEXT_SCENE:
                self.game.change_scene(self.NEXT_SCENE)
    
    def _apply_line_effects(self, line):
        pass
    
    def _on_choice_made(self, option):
        states_before = {}
        for sprite_id, rel in self.relationships.items():
            states_before[sprite_id] = rel.get_all().copy()
        tags_before = self.game.player_tags.get_all().copy()
        
        rel_changes = {}
        for sprite_id, rel in self.relationships.items():
            changes = {}
            for param in rel.params.keys():
                if param in option:
                    changes[param] = option[param]
            if changes:
                rel.modify(**changes)
                rel_changes[sprite_id] = changes
        
        tag_changes = {}
        for tag in ["curious", "kind", "aggressive"]:
            if tag in option:
                tag_changes[tag] = option[tag]
        
        if tag_changes:
            self.game.player_tags.add(**tag_changes)
        
        if hasattr(self.game, 'dialogue_history'):
            choice_question = ""
            all_options = []
            for i in range(self.current_dialogue, -1, -1):
                if self.dialogues[i].get("type") == "choice":
                    choice_question = self.dialogues[i].get("question", "")
                    all_options = self.dialogues[i].get("options", [])
                    break
            
            self.game.dialogue_history.record_choice(
                question=choice_question,
                selected_option=option,
                all_options=all_options,
                scene_name=self.name,
                effects={**tag_changes}
            )
            
            for sprite_id, rel in self.relationships.items():
                before = states_before[sprite_id]
                after = rel.get_all()
                if before != after:
                    self.game.dialogue_history.record_relationship_change(
                        sprt_id=sprite_id,
                        before=before,
                        after=after
                    )
            
            tags_after = self.game.player_tags.get_all()
            if tags_before != tags_after:
                self.game.dialogue_history.record_tags_change(
                    before=tags_before,
                    after=tags_after
                )
        
        print(f"[DEBUG] {self.__class__.__name__}: {self.relationships} | Tags: {self.game.player_tags.get_all()}")
        
        self._after_choice(option)
    
    def _after_choice(self, option):
        pass