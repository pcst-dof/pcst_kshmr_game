import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from algorithms.easy.player_tags import PlayerTags

def test_basic():
    tags = PlayerTags()
    
    # Начальное состояние
    assert tags.get_all() == {'curious': 0, 'kind': 0, 'aggressive': 0}
    
    # Добавляем теги
    tags.add(curious=5, kind=3)
    assert tags.get('curious') == 5
    assert tags.get('kind') == 3
    
    # Проверяем условия
    assert tags.check('curious >= 5') == True
    assert tags.check('curious >= 10') == False
    
    # Границы
    tags.add(curious=200)
    assert tags.get('curious') == 100  # максимум
    
    # Доминирующий тег
    assert tags.get_dominant() == 'curious'
    
    print("Все тесты PlayerTags пройдены")

if __name__ == "__main__":
    test_basic()