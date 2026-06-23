"""
Алгоритм 1 (Easy): Система отношений со спрутами.

Хранит внутри себя параметры восприятия ГГ глазами спрайта и предоставляет методы для изменения.
Каждый спрут может иметь свою систему отношений к ГГ.

"""


class Relationship:
    """Система отношений со спрутами.
    
    По умолчанию использует три параметра:
        trust: доверие (-10 до 10)
        fear: страх (-10 до 10)
        annoyance: раздражение (-10 до 10)
    """
    
    DEFAULT_PARAMS = {
        "trust": {"min": -10, "max": 10, "default": 0},
        "fear": {"min": -10, "max": 10, "default": 0},
        "annoyance": {"min": -10, "max": 10, "default": 0},
    }
    
    def __init__(self, sprt_id: str, custom_params: dict = None):
        """
            sprt_id: уникальный идентификатор спрута
            custom_params: переопределение границ параметров
        """
        self.sprt_id = sprt_id
        self.params = {}
        
        # Инициализация параметров
        params_config = custom_params or self.DEFAULT_PARAMS
        for param_name, config in params_config.items():
            self.params[param_name] = {
                "value": config.get("default", 0),
                "min": config.get("min", -10),
                "max": config.get("max", 10),
            }
    
    def modify(self, **changes):
        """
        Изменение параметров под допустимые.
        """
        for param_name, delta in changes.items():
            if param_name in self.params:
                p = self.params[param_name]
                p["value"] = max(p["min"], min(p["max"], p["value"] + delta))
    
    def get(self, param_name: str) -> int:
        """
        Получает значение параметра.
        """
        if param_name in self.params:
            return self.params[param_name]["value"]
        return 0
    
    def get_all(self) -> dict:
        """
        Получает все параметры.
        """
        return {name: p["value"] for name, p in self.params.items()}
    
    def get_dominant(self) -> str:
        """
        Определяет доминирующий параметр через абсолютное значение.
        """
        if not self.params:
            return None
        return max(self.params, key=lambda k: abs(self.params[k]["value"]))
    
    def check(self, condition: str) -> bool:
        """
        Проверяет условие на основе параметров.
        """
        safe_expr = condition
        for param_name, p in self.params.items():
            safe_expr = safe_expr.replace(param_name, str(p["value"]))
        
        # Разрешаем только безопасные операции
        allowed_chars = set("0123456789<>=!&|() .")
        if not all(c in allowed_chars for c in safe_expr):
            return False
        
        try:
            return bool(eval(safe_expr, {"__builtins__": {}}, {}))
        except Exception:
            return False
    
    def get_emotion(self, thresholds: dict = None) -> str:
        """
        Получает эмоцию по параметрам:

        {"happy": "trust >= 5", "angry": "annoyance >= 5"}
        не указан - базовая логика.
        """
        if thresholds:
            for emotion, condition in thresholds.items():
                if self.check(condition):
                    return emotion
            return "neutral"
        
        # Базовая логика
        if self.get("trust") >= 5:
            return "happy"
        elif self.get("fear") >= 5 or self.get("annoyance") >= 5:
            return "angry"
        return "neutral"
    
    def is_high(self, param_name: str, threshold: int = 5) -> bool:
        return self.get(param_name) >= threshold
    
    def is_low(self, param_name: str, threshold: int = -5) -> bool:
        return self.get(param_name) <= threshold
    
    def reset(self):
        """
        Сбрасывает параметры к изначальным значениям.
        """
        for param_name, p in self.params.items():
            p["value"] = 0