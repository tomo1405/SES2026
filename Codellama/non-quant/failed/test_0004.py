import pytest
from src_0004 import task_func

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    random_dict = task_func(LETTERS)
    assert isinstance(random_dict, dict)
    assert all(isinstance(k, str) and isinstance(v, list) for k, v in random_dict.items())
    assert all(len(v) >= 1 and len(v) <= 10 for v in random_dict.values())
    assert all(isinstance(x, int) and x >= 0 and x <= 100 for v in random_dict.values() for x in v)
    assert all(k in LETTERS for k in random_dict.keys())
    assert all(np.mean(v) >= 0 and np.mean(v) <= 100 for k, v in random_dict.items())