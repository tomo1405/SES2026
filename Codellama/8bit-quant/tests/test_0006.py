import pytest
from src_0006 import task_func

def test_task_func():
    random_dict = task_func()
    assert isinstance(random_dict, dict)
    assert all(isinstance(k, str) and k.isalpha() for k in random_dict.keys())
    assert all(isinstance(v, list) and all(isinstance(i, int) for i in v) for v in random_dict.values())
    assert all(len(v) >= 1 and len(v) <= 10 for v in random_dict.values())
    assert all(sum(v) / len(v) >= 0 and sum(v) / len(v) <= 100 for v in random_dict.values())
    assert all(math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v)) >= 0 for v in random_dict.values())