import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.easy.relationship import Relationship
from algorithms.easy.player_tags import PlayerTags
from algorithms.easy.dialogue_filter import DialogueFilter

def test_basic():
    rel = Relationship("clown_1")
    tags = PlayerTags()
    filter = DialogueFilter(rel, tags)
    
    tags.add(curious=20)
    
    choices = [
        {"text": "Обычный выбор", "next": 1},
        {"text": "Секретный выбор", "next": 2, "condition": "curious >= 15"},
        {"text": "Недоступный выбор", "next": 3, "condition": "curious >= 50"},
    ]
    
    available = filter.filter_choices(choices)
    
    assert len(available) == 2
    assert available[0]["text"] == "Обычный выбор"
    assert available[1]["text"] == "Секретный выбор"
    
    print("Все тесты DialogueFilter пройдены")

if __name__ == "__main__":
    test_basic()