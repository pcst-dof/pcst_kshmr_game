import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.medium.dialogue_history import DialogueHistory

def test_basic():
    history = DialogueHistory()
    
    history.record_scene_change("main_menu", "0")
    history.record_line("Авель", "Ну и пылища тут.", "0")
    history.record_line("ГГ", "А чего ты ожидал?", "0")
    
    history.record_choice(
        question="Что ответить?",
        selected_option={"text": "А ты кто?", "next": 48},
        all_options=[
            {"text": "Сам по себе", "next": 30},
            {"text": "Мой друг", "next": 38},
            {"text": "А ты кто?", "next": 48},
        ],
        scene_name="0",
        effects={"interest": 3, "curious": 5}
    )
    
    history.record_scene_change("0", "1")
    
    assert len(history.entries) == 5
    assert len(history.get_choices()) == 1
    assert len(history.get_scene_changes()) == 2
    
    path = history.get_full_path()
    assert "0" in path
    assert "1" in path
    
    text = history.get_dialogue_text("0")
    assert "Авель" in text
    assert "А ты кто?" in text
    
    stats = history.get_stats()
    assert stats["total_choices"] == 1
    assert stats["scenes_visited"] == 3
    assert "main_menu" in stats["scenes_list"]
    assert "0" in stats["scenes_list"]
    assert "1" in stats["scenes_list"]
    
    print(text)
    print(f"\nПуть: {path}")
    print(f"Статистика: {stats}")
    print("\nВсе тесты DialogueHistory пройдены")

if __name__ == "__main__":
    test_basic()