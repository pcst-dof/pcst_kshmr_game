"""
Алгоритм 4 (Easy): Конечный автомат состояний сцен.

Формальная модель управления переходами между сценами.
Гарантирует, что переходы возможны только по заданным правилам.
"""


class SceneFSM:
    """Конечный автомат для управления сценами."""
    
    def __init__(self, strict_mode=False):
        """
        Args:
            strict_mode: если True, запрещает переходы, которых нет в списке.
                         если False - разрешает любые переходы.
        """
        self.states = set()
        self.transitions = {}
        self.strict_mode = strict_mode
    
    def add_state(self, name):
        """Добавить сцену."""
        self.states.add(name)
        if name not in self.transitions:
            self.transitions[name] = set()
    
    def add_transition(self, from_state, to_state):
        """Добавить разрешённый переход между состояниями."""
        self.add_state(from_state)
        self.add_state(to_state)
        self.transitions[from_state].add(to_state)
    
    def can_transition(self, from_state, to_state):
        """Проверить, возможен ли переход."""
        if from_state not in self.states:
            return False
        if to_state not in self.states:
            return False
        if not self.strict_mode:
            return True
        return to_state in self.transitions.get(from_state, set())
    
    def transition(self, from_state, to_state):
        """Выполнить переход."""
        if self.can_transition(from_state, to_state):
            return True
        
        if self.strict_mode:
            print(f"[FSM] Запрещён переход: {from_state} → {to_state}")
            return False
        
        return False
    
    def get_available_transitions(self, state):
        """Получить все доступные переходы из состояния."""
        if state not in self.states:
            return []
        
        if self.strict_mode:
            return list(self.transitions.get(state, set()))
        
        return list(self.states - {state})
    
    def get_states(self):
        """Получить все состояния."""
        return list(self.states)
    
    def is_valid_state(self, name):
        """Проверить, существует ли состояние."""
        return name in self.states
    
    def visualize(self):
        """Текстовое представление графа переходов."""
        lines = ["=== SceneFSM ==="]
        for state in sorted(self.states):
            targets = sorted(self.transitions.get(state, set()))
            if targets:
                lines.append(f"  {state} → {', '.join(targets)}")
            else:
                lines.append(f"  {state} → (тупик)")
        return "\n".join(lines)