import pytest
from src_0878 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def test_task_func():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    n_components = 2
    result = task_func(data, n_components)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)

def test_task_func_invalid_data():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    n_components = 2
    with pytest.raises(ValueError):
        task_func(data, n_components)

def test_task_func_invalid_n_components():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    n_components = 3
    with pytest.raises(ValueError):
        task_func(data, n_components)

def test_task_func_invalid_data_type():
    data = [1, 2, 3]
    n_components = 2
    with pytest.raises(ValueError):
        task_func(data, n_components)

def test_task_func_invalid_data_values():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    n_components = 2
    data['a'] = 'a'
    with pytest.raises(ValueError):
        task_func(data, n_components)