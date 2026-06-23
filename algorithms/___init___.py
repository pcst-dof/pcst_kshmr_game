"""
Модуль алгоритмов игры.

Структура:
- easy/     — простые алгоритмы (4 штуки)
- medium/   — средние алгоритмы (2 штуки)
- hard/     — сложные алгоритмы
"""

from algorithms.easy import Relationship, PlayerTags, DialogueFilter, SceneFSM
from algorithms.medium import DialogueTree, DialogueNode, DialogueHistory

__all__ = [
    "Relationship",
    "PlayerTags", 
    "DialogueFilter",
    "SceneFSM",
    "DialogueTree",
    "DialogueNode",
    "DialogueHistory",
]