import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.medium.dialogue_tree import DialogueTree

def test_basic():
    dialogues = [
        {"type": "line", "speaker": "ГГ", "text": "Привет"},
        {
            "type": "choice",
            "question": "Выбери",
            "options": [
                {"text": "Вариант А", "next": 2},
                {"text": "Вариант Б", "next": 3},
            ]
        },
        {"type": "line", "speaker": "Клоун", "text": "Ты выбрал А", "next_scene": "ending_a"},
        {"type": "line", "speaker": "Клоун", "text": "Ты выбрал Б", "next_scene": "ending_b"},
    ]
    
    tree = DialogueTree()
    tree.build_from_dialogues(dialogues)
    
    assert tree.get_node_count() == 4
    assert tree.get_choice_count() == 1
    assert tree.root.index == 0
    
    endings = tree.find_all_endings()
    assert len(endings) == 2
    
    ending_scenes = {e["ending"] for e in endings}
    assert "ending_a" in ending_scenes
    assert "ending_b" in ending_scenes
    
    path = tree.find_shortest_path(3)
    assert path is not None
    assert path[-1] == 3
    
    stats = tree.get_stats()
    assert stats["total_nodes"] == 4
    assert stats["choices"] == 1
    assert stats["total_endings"] == 2
    
    print(tree.visualize())
    print(f"\nСтатистика: {stats}")
    print("\nВсе тесты DialogueTree пройдены")

if __name__ == "__main__":
    test_basic()