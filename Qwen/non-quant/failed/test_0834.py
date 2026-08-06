import pytest
from src_0834 import task_func
from statistics import mode
from collections import Counter

def test_task_func_default_parameters():
    result_mode, result_numbers = task_func()
    assert isinstance(result_mode, int)
    assert isinstance(result_numbers, list)
    for number, count in result_numbers:
        assert isinstance(number, int)
        assert isinstance(count, int)

def test_task_func_custom_parameters():
    result_mode, result_numbers = task_func(list_length=500, range_start=5, range_end=15, random_seed=42)
    assert isinstance(result_mode, int)
    assert isinstance(result_numbers, list)
    for number, count in result_numbers:
        assert isinstance(number, int)
        assert isinstance(count, int)
        assert 5 <= number <= 15

def test_task_func_mode_consistency():
    random_seed = 42
    expected_mode, _ = task_func(random_seed=random_seed)
    result_mode, _ = task_func(random_seed=random_seed)
    assert expected_mode == result_mode

def test_task_func_counter_consistency():
    random_seed = 42
    _, expected_numbers = task_func(random_seed=random_seed)
    _, result_numbers = task_func(random_seed=random_seed)
    expected_counter = Counter(dict(expected_numbers))
    result_counter = Counter(dict(result_numbers))
    assert expected_counter == result_counter

def test_task_func_no_elements():
    with pytest.raises(StatisticsError):
        task_func(list_length=0)