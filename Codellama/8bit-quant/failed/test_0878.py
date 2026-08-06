import pytest
from src_0878 import task_func
import pandas as pd

def test_task_func_data_type():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(data, n_components=2)

def test_task_func_data_values():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(data, n_components=2)

def test_task_func_n_components():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(data, n_components=2)

def test_task_func_output():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    output = task_func(data, n_components=2)
    assert isinstance(output, pd.DataFrame)
    assert output.shape == (3, 2)