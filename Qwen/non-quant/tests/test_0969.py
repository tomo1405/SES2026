import pytest
import seaborn as sns
from src_0969 import task_func


def test_task_func_no_numeric_columns():
    data = {'col1': ['a', 'b', 'c'], 'col2': ['d', 'e', 'f']}
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "No numeric columns present"

def test_task_func_with_numeric_columns():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_mixed_columns():
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [4.5, 5.5, 6.5]}
    ax = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_empty_data():
    data = {}
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "No numeric columns present"