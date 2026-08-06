import statistics

from src_0201 import task_func


def test_task_func_with_n_less_than_1():
    result = task_func(0, 0.5)
    assert result == ([], 0)

def test_task_func_with_n_equal_to_1():
    result = task_func(1, 0.5)
    assert len(result[0]) <= 1 and result[1] <= 1

def test_task_func_with_random_values():
    result = task_func(10, 0.5)
    assert isinstance(result[0], list)
    assert isinstance(result[1], int)
    assert all(x > statistics.mean(result[0]) for x in result[0])

def test_task_func_with_value_greater_than_all_numbers():
    result = task_func(10, 2.0)
    assert result[1] == 0

def test_task_func_with_value_less_than_all_numbers():
    result = task_func(10, -1.0)
    assert result[1] == 10

def test_task_func_with_value_equal_to_average():
    result = task_func(10, statistics.mean([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]))
    assert result[1] == 5