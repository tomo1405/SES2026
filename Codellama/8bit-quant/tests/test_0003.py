import statistics

from src_0003 import task_func


def test_task_func():
    LETTERS = ['A', 'B', 'C']
    random_dict = task_func(LETTERS)
    assert isinstance(random_dict, dict)
    assert all(isinstance(key, str) and isinstance(value, list) for key, value in random_dict.items())
    assert all(len(value) >= 1 and len(value) <= 10 for value in random_dict.values())
    assert all(isinstance(item, int) and item >= 0 and item <= 100 for sublist in random_dict.values() for item in sublist)
    assert all(key in LETTERS for key in random_dict.keys())
    assert all(statistics.mean(value) >= 0 for value in random_dict.values())
    assert all(statistics.mean(value) <= 100 for value in random_dict.values())