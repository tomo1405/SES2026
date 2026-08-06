import collections
import random
import string

from src_0395 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) <= length, "The number of unique characters should not exceed the length of the string"

def test_task_func_seed_consistency():
    length = 10
    seed = 42
    first_result = task_func(length, seed)
    second_result = task_func(length, seed)
    assert first_result == second_result, "Results should be consistent with the same seed"

def test_task_func_character_types():
    length = 10
    result = task_func(length)
    for char in result.keys():
        assert char in string.ascii_letters, "Characters should be ASCII letters"

def test_task_func_counter_correctness():
    length = 10
    seed = 42
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    expected_counter = dict(collections.Counter(random_string))
    result = task_func(length, seed)
    assert result == expected_counter, "The character frequency counter should match the expected result"

def test_task_func_empty_string():
    length = 0
    result = task_func(length)
    assert result == {}, "An empty string should return an empty dictionary"