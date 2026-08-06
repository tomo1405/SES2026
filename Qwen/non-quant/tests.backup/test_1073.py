import pytest
from src_1073 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_empty_input():
    result = task_func([])
    assert result == []

def test_task_func_with_single_sublist():
    input_data = [['a', 'b', 'c']]
    result = task_func(input_data)
    assert len(result) == 1
    assert isinstance(result[0], pd.Series)
    assert result[0].index.tolist() == ['a', 'b', 'c']
    assert all(isinstance(value, int) for value in result[0].values)

def test_task_func_with_multiple_sublists():
    input_data = [['x', 'y'], ['m', 'n', 'o']]
    result = task_func(input_data)
    assert len(result) == 2
    assert isinstance(result[0], pd.Series)
    assert result[0].index.tolist() == ['x', 'y']
    assert all(isinstance(value, int) for value in result[0].values)
    assert isinstance(result[1], pd.Series)
    assert result[1].index.tolist() == ['m', 'n', 'o']
    assert all(isinstance(value, int) for value in result[1].values)

def test_task_func_with_duplicate_indices():
    input_data = [['a', 'b', 'a']]
    with pytest.raises(ValueError):
        task_func(input_data)

def test_task_func_with_non_string_indices():
    input_data = [[1, 2, 3]]
    result = task_func(input_data)
    assert len(result) == 1
    assert isinstance(result[0], pd.Series)
    assert result[0].index.tolist() == [1, 2, 3]
    assert all(isinstance(value, int) for value in result[0].values)

def test_task_func_with_large_sublist():
    input_data = [['item' + str(i) for i in range(100)]]
    result = task_func(input_data)
    assert len(result) == 1
    assert isinstance(result[0], pd.Series)
    assert result[0].index.tolist() == ['item' + str(i) for i in range(100)]
    assert all(isinstance(value, int) for value in result[0].values)