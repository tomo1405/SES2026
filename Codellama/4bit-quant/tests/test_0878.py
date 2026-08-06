import pandas as pd
import pytest
from src_0878 import task_func


def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 2
    result = task_func(data, n_components)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
    assert result.columns.to_list() == ['A', 'B']

def test_task_func_invalid_data():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 2
    with pytest.raises(ValueError):
        task_func(data, n_components)

def test_task_func_invalid_n_components():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 3
    with pytest.raises(ValueError):
        task_func(data, n_components)