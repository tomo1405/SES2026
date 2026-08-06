import pytest
from src_0332 import task_func

def test_task_func_returns_correct_list():
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    expected_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    expected_list.insert(bisect.bisect(expected_list, num), num)
    assert task_func(num, list_length, min_value, max_value) == (expected_list, expected_list)

def test_task_func_returns_correct_sorted_list():
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    expected_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    expected_list.insert(bisect.bisect(expected_list, num), num)
    assert task_func(num, list_length, min_value, max_value)[1] == sorted(expected_list)

def test_task_func_returns_correct_length():
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    expected_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    expected_list.insert(bisect.bisect(expected_list, num), num)
    assert len(task_func(num, list_length, min_value, max_value)[0]) == list_length

def test_task_func_returns_correct_min_value():
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    expected_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    expected_list.insert(bisect.bisect(expected_list, num), num)
    assert min(task_func(num, list_length, min_value, max_value)[0]) == min_value

def test_task_func_returns_correct_max_value():
    num = 5
    list_length = 5
    min_value = 0
    max_value = 10
    expected_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    expected_list.insert(bisect.bisect(expected_list, num), num)
    assert max(task_func(num, list_length, min_value, max_value)[0]) == max_value