from typing import Counter

from src_0893 import task_func


def test_task_func_empty_list():
    assert task_func([]) == Counter()

def test_task_func_single_string_no_pattern():
    assert task_func(["no_pattern_here"]) == Counter({0: 1})

def test_task_func_single_string_with_pattern():
    assert task_func(["}"]) == Counter({1: 1})

def test_task_func_multiple_strings_no_pattern():
    assert task_func(["a", "b", "c"]) == Counter({0: 3})

def test_task_func_multiple_strings_with_patterns():
    assert task_func(["}", "}}", "}}}"]) == Counter({1: 1, 2: 1, 3: 1})

def test_task_func_random_strings():
    strings = ["}", "}}", "}}}", "a", "b", "c"]
    result = task_func(strings)
    assert all(count <= 3 for count in result.keys())
    assert sum(result.values()) == 10

def test_task_func_large_input():
    strings = ["]" * i for i in range(100)]
    result = task_func(strings)
    assert len(result) <= 10
    assert sum(result.values()) == 10