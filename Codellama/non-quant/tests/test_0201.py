import random

from src_0201 import task_func


def test_task_func_n_less_than_1():
    n = 0
    value = 0.5
    expected_greater_avg = []
    expected_num_greater_value = 0

    greater_avg, num_greater_value = task_func(n, value)

    assert greater_avg == expected_greater_avg
    assert num_greater_value == expected_num_greater_value

def test_task_func_n_greater_than_1():
    n = 10
    value = 0.5
    expected_greater_avg = [random.random() for _ in range(n)]
    expected_num_greater_value = len(expected_greater_avg)

    greater_avg, num_greater_value = task_func(n, value)

    assert greater_avg == expected_greater_avg
    assert num_greater_value == expected_num_greater_value

def test_task_func_value_less_than_avg():
    n = 10
    value = 0.5
    expected_greater_avg = [random.random() for _ in range(n)]
    expected_num_greater_value = len(expected_greater_avg)

    greater_avg, num_greater_value = task_func(n, value)

    assert greater_avg == expected_greater_avg
    assert num_greater_value == expected_num_greater_value

def test_task_func_value_greater_than_avg():
    n = 10
    value = 0.5
    expected_greater_avg = [random.random() for _ in range(n)]
    expected_num_greater_value = len(expected_greater_avg)

    greater_avg, num_greater_value = task_func(n, value)

    assert greater_avg == expected_greater_avg
    assert num_greater_value == expected_num_greater_value