import pandas as pd
import pytest
from src_0577 import task_func


def test_task_func_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_single_element():
    result = task_func(['a'])
    assert result.equals(pd.Series(['a']))

def test_task_func_multiple_elements():
    result = task_func(['abc', 'def'])
    assert isinstance(result, pd.Series)
    assert len(result) == 10  # 2 elements * 5 groups

def test_task_func_single_character_elements():
    result = task_func(['a', 'b', 'c'])
    assert result.equals(pd.Series(['a', 'b', 'c'] * 5))

def test_task_func_n_groups():
    result = task_func(['abc'], n_groups=3)
    assert len(result) == 3

def test_task_func_randomness():
    result1 = task_func(['abc', 'def'])
    result2 = task_func(['abc', 'def'])
    assert not result1.equals(result2)  # Due to randomness, results should differ

def test_task_func_large_input():
    result = task_func(['x' * 1000] * 10, n_groups=10)
    assert len(result) == 100

def test_task_func_non_string_elements():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_invalid_n_groups():
    with pytest.raises(ValueError):
        task_func(['a'], n_groups=-1)