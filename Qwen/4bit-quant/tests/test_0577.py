import pandas as pd
import pytest
from src_0577 import task_func


def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_element():
    result = task_func(['a'], 3)
    assert result.equals(pd.Series(['a', 'a', 'a']))

def test_task_func_multiple_elements():
    result = task_func(['abc', 'def'], 2)
    assert len(result) == 4

def test_task_func_single_character_elements():
    result = task_func(['a', 'b', 'c'], 2)
    assert result.equals(pd.Series(['a', 'b', 'c', 'a', 'b', 'c']))

def test_task_func_large_group_size():
    result = task_func(['abc'], 10)
    assert len(result) == 10

def test_task_func_random_shifts():
    result = task_func(['abc'], 2)
    assert result[0] != 'abc' and result[0] in ['bca', 'cab']
    assert result[1] != 'abc' and result[1] in ['bca', 'cab']

def test_task_func_non_string_elements():
    with pytest.raises(TypeError):
        task_func([1, 2, 3], 2)

def test_task_func_invalid_n_groups():
    with pytest.raises(ValueError):
        task_func(['abc'], 0)