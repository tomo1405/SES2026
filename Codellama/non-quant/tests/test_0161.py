import pytest
from src_0161 import task_func
import pandas as pd
import seaborn as sns
from scipy import stats


def test_task_func_valid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    df, ax, p = task_func(data)
    assert df.shape[1] == 8
    assert df.columns.tolist() == COLUMN_NAMES
    assert df['Average'].tolist() == [10, 11, 12]
    assert ax.get_title() == 'Average'
    assert ax.get_xlabel() == 'Average'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_linewidth() == 3
    assert p is not None


def test_task_func_invalid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    with pytest.raises(ValueError):
        task_func(data)