import random
import string

from src_0768 import task_func


def test_task_func_empty_input():
    assert task_func([]) == {}

def test_task_func_single_empty_sublist():
    assert task_func([[]]) == {}

def test_task_func_multiple_empty_sublists():
    assert task_func([[], [], []]) == {}

def test_task_func_single_element_sublists():
    result = task_func([['a'], ['b'], ['c']])
    assert len(result) == 3
    for letter in 'abc':
        assert result[letter] == 1

def test_task_func_mixed_sublists():
    result = task_func([['a', 'b'], ['c'], ['d', 'e', 'f']])
    assert len(result) == 6
    for letter in 'abcdef':
        assert result[letter] == 1

def test_task_func_repeated_elements():
    result = task_func([['a', 'a'], ['b', 'b'], ['c', 'c']])
    assert len(result) == 3
    for letter in 'abc':
        assert result[letter] == 2

def test_task_func_large_input():
    result = task_func([[random.choice(string.ascii_letters) for _ in range(100)] for _ in range(10)])
    assert len(result) <= 52  # Only letters from string.ascii_letters
    for count in result.values():
        assert count >= 1 and count <= 100

def test_task_func_random_letters():
    random.seed(42)  # For reproducibility
    result = task_func([[random.choice(string.ascii_letters) for _ in range(10)] for _ in range(5)])
    expected = {'n': 1, 'r': 2, 's': 1, 'p': 1, 'k': 1, 'g': 1, 'w': 1, 'z': 1, 'h': 1, 'q': 1}
    assert result == expected