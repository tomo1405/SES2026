import pytest
from src_0849 import task_func

def test_task_func():
    obj_list = [
        {'a': 1, 'b': 2},
        {'a': 3, 'b': 4},
        {'a': 5, 'b': 6},
        {'a': 7, 'b': 8},
        {'a': 9, 'b': 10}
    ]
    top_n = 3
    seed = 1234

    top_values, random_value = task_func(obj_list, 'a', top_n, seed)

    assert top_values == [9, 7, 5]
    assert random_value == 3