"""
Простые алгоритмы.

Содержит 4 базовых алгоритма для игровой логики:
1. Relationship - система отношений со спрутами
2. PlayerTags - система тегов ГГ
3. DialogueFilter
4. SceneFSM
"""

from algorithms.easy.relationship import Relationship
from algorithms.easy.player_tags import PlayerTags
from algorithms.easy.dialogue_filter import DialogueFilter
from algorithms.easy.scene_fsm import SceneFSM

__all__ = ["Relationship", "PlayerTags", "DialogueFilter", "SceneFSM"]