"""
Алгоритм 2 (Easy): Система тегов игрока.

Скрытые характеристики игрока, накапливающиеся в процессе игры.
В отличие от Relationship, теги растут.
Влияют на доступные диалоги и реакции спрутов.
"""


class PlayerTags:
    """Система тегов игрока.
    
    Параметры:
        curious: любопытство (0 до 100)
        kind: доброта (0 до 100)
        aggressive: агрессия (0 до 100)
    """
    
    DEFAULT_TAGS = {
        "curious": {"max": 100, "default": 0},
        "kind": {"max": 100, "default": 0},
        "aggressive": {"max": 100, "default": 0},
    }
    
    def __init__(self, custom_tags=None):
        self.tags = {}
        
        tags_config = custom_tags or self.DEFAULT_TAGS
        for tag_name, config in tags_config.items():
            self.tags[tag_name] = {
                "value": config.get("default", 0),
                "max": config.get("max", 100),
            }
    
    def add(self, **changes):
        """
        Добавить значения к тегам.
        """
        for tag_name, delta in changes.items():
            if tag_name in self.tags:
                t = self.tags[tag_name]
                t["value"] = min(t["max"], t["value"] + delta)
    
    def get(self, tag_name: str) -> int:
        """
        Получить значение тега.
        """
        if tag_name in self.tags:
            return self.tags[tag_name]["value"]
        return 0
    
    def get_all(self) -> dict:
        """
        Получить все теги.
        """
        return {name: t["value"] for name, t in self.tags.items()}
    
    def get_dominant(self) -> str:
        """
        Определить доминирующий тег.
        """
        if not self.tags:
            return None
        return max(self.tags, key=lambda k: self.tags[k]["value"])
    
    def check(self, condition: str) -> bool:
        """
        Проверить условие на основе тегов.
        """
        safe_expr = condition
        for tag_name, t in self.tags.items():
            safe_expr = safe_expr.replace(tag_name, str(t["value"]))
        
        allowed_chars = set("0123456789<>=!&|() .")
        if not all(c in allowed_chars for c in safe_expr):
            return False
        
        try:
            return bool(eval(safe_expr, {"__builtins__": {}}, {}))
        except Exception:
            return False
    
    def is_high(self, tag_name: str, threshold: int = 50) -> bool:
        return self.get(tag_name) >= threshold
    
    def reset(self):
        """
        Сбросить все теги к начальным значениям.
        """
        for tag_name, t in self.tags.items():
            t["value"] = 0