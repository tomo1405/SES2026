import pytest
from src_0893 import task_func

def test_task_func():
    strings = ['hello', 'world', 'goodbye']
    pattern_counts = task_func(strings)
    assert pattern_counts == Counter({'{': 1})

def test_task_func_empty_list():
    strings = []
    pattern_counts = task_func(strings)
    assert pattern_counts == Counter()

def test_task_func_invalid_input():
    strings = ['hello', 'world', 'goodbye']
    pattern_counts = task_func(strings)
    assert pattern_counts == Counter()