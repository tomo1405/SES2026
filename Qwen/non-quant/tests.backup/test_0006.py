import pytest
from src_0006 import task_func
import random
import math

def test_task_func_keys():
    result = task_func()
    assert set(result.keys()) == set(chr(i) for i in range(97, 123))

def test_task_func_values_length():
    result = task_func()
    for values in result.values():
        assert 1 <= len(values) <= 10

def test_task_func_values_range():
    result = task_func()
    for values in result.values():
        for value in values:
            assert 0 <= value <= 100

def test_task_func_std_deviation():
    random.seed(0)  # Ensure reproducibility
    expected_result = {
        'a': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'b': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'c': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'd': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'e': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'f': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'g': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'h': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'i': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'j': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'k': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'l': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'm': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'n': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'o': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'p': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'q': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'r': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        's': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        't': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'u': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'v': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'w': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'x': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'y': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2),
        'z': math.sqrt(sum((i - 48.5) ** 2 for i in [46, 51]) / 2)
    }
    result = task_func()
    assert result == expected_result

def test_task_func_with_custom_letters():
    custom_letters = ['a', 'b', 'c']
    result = task_func(custom_letters)
    assert set(result.keys()) == set(custom_letters)
    for values in result.values():
        assert 1 <= len(values) <= 10
        for value in values:
            assert 0 <= value <= 100