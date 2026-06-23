"""
Алгоритм 3 (Easy): Фильтр диалогов.

Фильтрует доступные варианты выбора на основе условий.
Использует Relationship и PlayerTags для проверки условий.
"""


class DialogueFilter:
    """Фильтр доступных реплик и выборов."""
    
    def __init__(self, relationship=None, player_tags=None):
        self.relationship = relationship
        self.player_tags = player_tags
    
    def filter_choices(self, choices: list) -> list:
        """Фильтрует список выборов, оставляя только доступные."""
        available = []
        
        for choice in choices:
            condition = choice.get("condition")
            
            if not condition:
                available.append(choice)
                continue
            
            if self._check_condition(condition):
                available.append(choice)
        
        return available
    
    def _check_condition(self, condition: str) -> bool:
        """Проверяет условие через Relationship и PlayerTags."""
        if self.player_tags and self.player_tags.check(condition):
            return True
        
        if self.relationship and self.relationship.check(condition):
            return True
        
        return False
    
    def is_available(self, condition: str) -> bool:
        """Проверяет доступность конкретного условия."""
        return self._check_condition(condition)