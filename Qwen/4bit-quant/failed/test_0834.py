import pytest
from src_0834 import task_func
from collections import Counter
from statistics import mode

def test_task_func_default_values():
    result_mode, numbers = task_func()
    assert isinstance(result_mode, int)
    assert isinstance(numbers, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in numbers)

def test_task_func_custom_range():
    result_mode, numbers = task_func(range_start=5, range_end=15)
    assert isinstance(result_mode, int)
    assert isinstance(numbers, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in numbers)
    assert all(5 <= number <= 15 for number, count in numbers)

def test_task_func_custom_length():
    result_mode, numbers = task_func(list_length=500)
    assert isinstance(result_mode, int)
    assert isinstance(numbers, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in numbers)
    assert len(numbers) <= 500

def test_task_func_random_seed():
    seed_value = 42
    result_mode_1, numbers_1 = task_func(random_seed=seed_value)
    result_mode_2, numbers_2 = task_func(random_seed=seed_value)
    assert result_mode_1 == result_mode_2
    assert numbers_1 == numbers_2

def test_task_func_mode_accuracy():
    seed_value = 42
    result_mode, numbers = task_func(random_seed=seed_value)
    counter = Counter([num for num, _ in numbers])
    assert result_mode == max(counter, key=counter.get)

def test_task_func_empty_list():
    with pytest.raises(StatisticsError):
        task_func(list_length=0)

def test_task_func_single_element_list():
    seed_value = 42
    result_mode, numbers = task_func(list_length=1, random_seed=seed_value)
    assert len(numbers) == 1
    assert result_mode == numbers[0][0]