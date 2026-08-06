import pytest
from src_0004 import task_func

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    random_dict = task_func(LETTERS)
    assert isinstance(random_dict, dict)
    assert all(isinstance(key, str) for key in random_dict.keys())
    assert all(isinstance(value, list) for value in random_dict.values())
    assert all(isinstance(item, int) for sublist in random_dict.values() for item in sublist)
    assert all(len(sublist) <= 10 for sublist in random_dict.values())
    assert all(0 <= item <= 100 for sublist in random_dict.values() for item in sublist)
    assert all(np.mean(sublist) == mean_dict[key] for key, sublist in random_dict.items())