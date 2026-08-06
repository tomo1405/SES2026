import numpy as np
import pytest
import seaborn as sns
from src_0969 import task_func


def test_task_func_with_numeric_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['a', 'b', 'c']
    }
    ax = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_no_numeric_data():
    data = {
        'A': ['a', 'b', 'c'],
        'B': ['d', 'e', 'f']
    }
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "No numeric columns present"

def test_task_func_with_empty_data():
    data = {}
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "No numeric columns present"

def test_task_func_with_all_null_values():
    data = {
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    }
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "No numeric columns present"