import pytest
from src_0336 import task_func

def test_task_func():
    assert task_func(100) == {'a': 22, 'b': 20, 'c': 19, 'd': 18, 'e': 17}
    assert task_func(5) == {'e': 5, 'a': 4, 'b': 3, 'd': 2, 'c': 1}
    assert task_func(1) == {'e': 1}
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(-1)