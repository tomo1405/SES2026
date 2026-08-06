import pytest
from src_0893 import task_func

# Test cases
def test_empty_list():
    assert task_func([]) == Counter()

def test_single_string():
    assert task_func(["a"]) == Counter({0: 1})

def test_multiple_strings():
    assert task_func(["a", "aa", "aaa"]) == Counter({2: 1, 0: 1})

def test_random_choices():
    random.seed(0)
    assert task_func(["a", "aa", "aaa"]) == Counter({2: 1, 0: 1})

def test_empty_input():
    assert task_func([]) == Counter()