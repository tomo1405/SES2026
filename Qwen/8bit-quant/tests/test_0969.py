import pytest
import seaborn as sns
from src_0969 import task_func


def test_task_func_no_numeric_columns():
    data = {
        'A': ['a', 'b', 'c'],
        'B': ['d', 'e', 'f']
    }
    with pytest.raises(ValueError, match="No numeric columns present"):
        task_func(data)

def test_task_func_with_numeric_columns():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    ax = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_mixed_columns():
    data = {
        'A': [1, 2, 3],
        'B': ['d', 'e', 'f'],
        'C': [4.5, 5.5, 6.5]
    }
    ax = task_func(data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)