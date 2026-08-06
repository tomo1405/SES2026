import random
import string

import pytest
from src_0821 import task_func


def test_task_func_positive_values():
    result = task_func(3, 5)
    assert len(result) == 3
    for word in result:
        assert len(word) == 5
        assert all(char in string.ascii_letters for char in word)

def test_task_func_zero_values():
    result = task_func(0, 0)
    assert result == []

def test_task_func_single_word():
    result = task_func(1, 1)
    assert len(result) == 1
    assert len(result[0]) == 1
    assert result[0] in string.ascii_letters

def test_task_func_large_word_length():
    result = task_func(1, 100)
    assert len(result) == 1
    assert len(result[0]) == 100
    assert all(char in string.ascii_letters for char in result[0])

def test_task_func_negative_num_words():
    with pytest.raises(ValueError) as excinfo:
        task_func(-1, 5)
    assert str(excinfo.value) == "num_words and word_length must be non-negative"

def test_task_func_negative_word_length():
    with pytest.raises(ValueError) as excinfo:
        task_func(5, -1)
    assert str(excinfo.value) == "num_words and word_length must be non-negative"

def test_task_func_both_negative():
    with pytest.raises(ValueError) as excinfo:
        task_func(-1, -1)
    assert str(excinfo.value) == "num_words and word_length must be non-negative"

def test_task_func_reproducibility():
    random.seed(42)
    first_run = task_func(3, 5)
    random.seed(42)
    second_run = task_func(3, 5)
    assert first_run == second_run