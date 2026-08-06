import pandas as pd
import pytest
from src_0936 import task_func


def test_task_func_empty_word():
    word = ''
    expected_output = pd.DataFrame({'Letter': [], 'Position': []})
    assert task_func(word).equals(expected_output)

def test_task_func_invalid_word():
    word = 'hello123'
    with pytest.raises(ValueError):
        task_func(word)

def test_task_func_valid_word():
    word = 'hello'
    expected_output = pd.DataFrame({'Letter': ['h', 'e', 'l', 'l', 'o'], 'Position': [1, 2, 3, 4, 5]})
    assert task_func(word).equals(expected_output)