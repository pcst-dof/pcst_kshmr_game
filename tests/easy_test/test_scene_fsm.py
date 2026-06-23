import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.easy.scene_fsm import SceneFSM

def test_basic():
    fsm = SceneFSM(strict_mode=True)
    
    fsm.add_state("main_menu")
    fsm.add_state("place_0")
    fsm.add_state("place_1")
    fsm.add_state("ending")
    
    fsm.add_transition("main_menu", "place_0")
    fsm.add_transition("place_0", "place_1")
    fsm.add_transition("place_1", "ending")
    
    assert fsm.can_transition("main_menu", "place_0") == True
    assert fsm.can_transition("main_menu", "ending") == False
    assert fsm.can_transition("place_1", "main_menu") == False
    
    assert fsm.transition("main_menu", "place_0") == True
    assert fsm.transition("main_menu", "ending") == False
    
    available = fsm.get_available_transitions("main_menu")
    assert "place_0" in available
    
    print("\n" + fsm.visualize())
    print("\nВсе тесты SceneFSM пройдены")

if __name__ == "__main__":
    test_basic()