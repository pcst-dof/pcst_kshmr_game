"""
Алгоритм (Medium): История диалогов.

Хранит последовательность действий игрока:
- Пройденные реплики
- Сделанные выборы
- Изменения отношений и тегов

Использует DialogueTree для валидации и отображения пути.
"""


class DialogueHistory:
    """История действий игрока в диалогах."""
    
    def __init__(self):
        self.entries = []
        self.current_scene = None
    
    def record_line(self, speaker, text, scene_name=None):
        """Записывает реплику в историю."""
        self.entries.append({
            "type": "line",
            "scene": scene_name or self.current_scene,
            "speaker": speaker,
            "text": text,
        })
    
    def record_choice(self, question, selected_option, all_options, scene_name=None, effects=None):
        """Записывает сделанный выбор."""
        self.entries.append({
            "type": "choice",
            "scene": scene_name or self.current_scene,
            "question": question,
            "selected": selected_option,
            "all_options": all_options,
            "effects": effects or {},
        })
    
    def record_choice_prompt(self, question, options, scene_name=None):
        """Записывает появление выбора."""
        self.entries.append({
            "type": "choice_prompt",
            "scene": scene_name or self.current_scene,
            "question": question,
            "options": options,
        })
    
    def record_scene_change(self, from_scene, to_scene):
        """Записывает переход между сценами."""
        self.entries.append({
            "type": "scene_change",
            "from": from_scene,
            "to": to_scene,
        })
        self.current_scene = to_scene
    
    def record_relationship_change(self, sprt_id, before, after):
        """Записывает изменение отношений."""
        self.entries.append({
            "type": "relationship_change",
            "sprt_id": sprt_id,
            "before": before,
            "after": after,
        })
    
    def record_tags_change(self, before, after):
        """Записывает изменение тегов игрока."""
        self.entries.append({
            "type": "tags_change",
            "before": before,
            "after": after,
        })
    
    def get_entries_by_scene(self, scene_name):
        """Возвращает все записи для конкретной сцены."""
        return [e for e in self.entries if e.get("scene") == scene_name]
    
    def get_choices(self):
        """Возвращает только сделанные выборы."""
        return [e for e in self.entries if e["type"] == "choice"]
    
    def get_scene_changes(self):
        """Возвращает все переходы между сценами."""
        return [e for e in self.entries if e["type"] == "scene_change"]
    
    def get_full_path(self):
        """Возвращает путь игрока как список сцен."""
        path = []
        for entry in self.entries:
            if entry["type"] == "scene_change":
                if not path or path[-1] != entry["to"]:
                    path.append(entry["to"])
            elif entry.get("scene") and entry["scene"] not in path:
                path.append(entry["scene"])
        return path
    
    def get_dialogue_text(self, scene_name=None):
        """Возвращает полный текст диалога для сцены (или всей игры)."""
        entries = self.get_entries_by_scene(scene_name) if scene_name else self.entries
        lines = []
        
        for entry in entries:
            if entry["type"] == "line":
                speaker = entry.get("speaker", "")
                text = entry.get("text", "")
                if speaker:
                    lines.append(f"{speaker}: {text}")
                else:
                    lines.append(text)
            
            elif entry["type"] == "choice":
                lines.append(f"\n[ВЫБОР] {entry['question']}")
                for i, opt in enumerate(entry["all_options"]):
                    marker = "→ " if opt == entry["selected"] else "  "
                    lines.append(f"{marker}{i+1}. {opt['text']}")
                lines.append("")
            
            elif entry["type"] == "choice_prompt":
                lines.append(f"\n[ВЫБОР] {entry['question']}")
                for i, opt in enumerate(entry.get("options", [])):
                    lines.append(f"  {i+1}. {opt['text']}")
                lines.append("")
            
            elif entry["type"] == "scene_change":
                lines.append(f"\n--- Переход: {entry['from']} → {entry['to']} ---\n")
            
            elif entry["type"] == "relationship_change":
                lines.append(f"[Отношения с {entry['sprt_id']}]: {entry['before']} → {entry['after']}")
            
            elif entry["type"] == "tags_change":
                lines.append(f"[Теги игрока]: {entry['before']} → {entry['after']}")
        
        return "\n".join(lines)
    
    def get_stats(self):
        """Статистика истории."""
        choices = self.get_choices()
        scenes = set()
        
        for entry in self.entries:
            if entry.get("scene"):
                scenes.add(entry["scene"])
            
            if entry["type"] == "scene_change":
                if entry.get("from"):
                    scenes.add(entry["from"])
                if entry.get("to"):
                    scenes.add(entry["to"])
        
        return {
            "total_entries": len(self.entries),
            "total_choices": len(choices),
            "scenes_visited": len(scenes),
            "scenes_list": sorted(scenes),
        }
    
    def clear(self):
        """Очищает историю."""
        self.entries.clear()
        self.current_scene = None
    
    def to_dict(self):
        """Сериализация для сохранения."""
        return {
            "entries": self.entries,
            "current_scene": self.current_scene,
        }
    
    @classmethod
    def from_dict(cls, data):
        """Десериализация из сохранения."""
        history = cls()
        history.entries = data.get("entries", [])
        history.current_scene = data.get("current_scene")
        return history