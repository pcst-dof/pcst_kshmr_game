import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.easy.relationship import Relationship

def test_basic():
    rel = Relationship("clown_1", custom_params={
        "interest":   {"min": -10, "max": 10, "default": 0},
        "obsession":  {"min": 0,   "max": 10, "default": 0},
        "resistance": {"min": 0,   "max": 5,  "default": 0},
    })
    
    assert rel.get_all() == {'interest': 0, 'obsession': 0, 'resistance': 0}
    
    rel.modify(interest=3)
    assert rel.get('interest') == 3
    
    rel.modify(interest=100)
    assert rel.get('interest') == 10
    
    assert rel.check('interest >= 5') == True
    
    print("Все тесты пройдены")

if __name__ == "__main__":
    test_basic()