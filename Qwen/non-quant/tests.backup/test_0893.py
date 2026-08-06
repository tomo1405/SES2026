import pytest
from src_0893 import task_func
from collections import Counter

def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_single_string_no_pattern():
    assert task_func(['no_pattern_here']) == Counter({0: 1})

def test_task_func_single_string_with_pattern():
    assert task_func(['}'] * 10) == Counter({1: 10})

def test_task_func_multiple_strings_no_pattern():
    assert task_func(['no_pattern', 'here_either']) == Counter({0: 10})

def test_task_func_multiple_strings_with_patterns():
    strings = ['}', '}}', '{}', '}{', '}}{', '{}}']
    result = task_func(strings)
    assert all(count <= 10 for count in result.values())

def test_task_func_pattern_count_distribution():
    strings = ['}' * i for i in range(11)]
    result = task_func(strings)
    assert sum(result.values()) == 10
    assert all(0 <= count <= 10 for count in result.values())

def test_task_func_random_behavior():
    strings = [str(i) for i in range(20)]
    result1 = task_func(strings)
    result2 = task_func(strings)
    assert result1 != result2  # Randomness should lead to different results