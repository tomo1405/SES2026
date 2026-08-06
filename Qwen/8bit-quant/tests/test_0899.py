from typing import Counter

from src_0899 import task_func


def test_task_func_with_default_seed():
    count = 10
    expected_output = Counter({('a', 'a'): 2, ('b', 'b'): 2, ('c', 'c'): 2, ('d', 'd'): 2, ('e', 'e'): 2})
    assert task_func(count) == expected_output

def test_task_func_with_custom_seed():
    count = 5
    seed = 42
    expected_output = Counter({('a', 'a'): 2, ('b', 'b'): 1, ('c', 'c'): 1, ('d', 'd'): 1})
    assert task_func(count, seed) == expected_output

def test_task_func_with_zero_count():
    count = 0
    expected_output = Counter()
    assert task_func(count) == expected_output

def test_task_func_with_large_count():
    count = 100
    seed = 123
    result = task_func(count, seed)
    assert len(result) <= len(LETTERS) ** 2

def test_task_func_with_single_letter_pairs():
    count = 5
    seed = 0
    expected_output = Counter({('a', 'a'): 2, ('b', 'b'): 1, ('c', 'c'): 1, ('d', 'd'): 1})
    assert task_func(count, seed) == expected_output