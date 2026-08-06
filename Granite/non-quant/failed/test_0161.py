import pandas as pd
import seaborn as sns
from scipy import stats
from src_0161 import task_func
import pytest

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def test_task_func_valid_input():
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    df, ax, p = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxisGrid)
    assert isinstance(p, (float, type(None)))

def test_task_func_invalid_input():
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_normaltest():
    data = [[1, 2, 3, 4, 5, 6, 7, 8] for _ in range(20)]
    df, ax, p = task_func(data)
    assert p < 0.05

def test_task_func_not_enough_samples():
    data = [[1, 2, 3, 4, 5, 6, 7, 8] for _ in range(10)]
    df, ax, p = task_func(data)
    assert p is None