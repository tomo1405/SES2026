import pytest
from src_0893 import task_func

def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_non_empty_list():
    strings = ['hello', 'world', 'goodbye']
    pattern = '}'
    random_choices = random.choices(strings, k=10)
    pattern_counts = Counter([string.count(pattern) for string in random_choices])
    assert task_func(strings) == pattern_counts