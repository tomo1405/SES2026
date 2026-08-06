import re

import pytest
from src_0844 import task_func


def test_task_func_basic():
    result = task_func(1)
    assert isinstance(result, str)
    assert result.endswith('.')

def test_task_func_multiple_sentences():
    result = task_func(3)
    assert isinstance(result, str)
    assert result.count('.') == 3

def test_task_func_no_extra_spaces():
    result = task_func(1)
    assert '  ' not in result

def test_task_func_only_valid_characters():
    result = task_func(1)
    assert re.match(r'^[a-z\s.]+$', result)

def test_task_func_sentence_length():
    result = task_func(1)
    words = result.split()
    assert 5 <= len(words) <= 10

def test_task_func_randomness():
    result1 = task_func(1)
    result2 = task_func(1)
    assert result1 != result2  # This is probabilistic and may fail occasionally

def test_task_func_empty_word_list():
    original_word_list = task_func.WORD_LIST[:]
    task_func.WORD_LIST = []
    with pytest.raises(IndexError):
        task_func(1)
    task_func.WORD_LIST = original_word_list

def test_task_func_zero_sentences():
    result = task_func(0)
    assert result == ""

def test_task_func_negative_sentences():
    with pytest.raises(ValueError):
        task_func(-1)