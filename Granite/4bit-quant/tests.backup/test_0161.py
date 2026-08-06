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
    assert p is not None or len(df['Average']) >= 20

def test_task_func_invalid_input():
    data = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]
    with pytest.raises(ValueError):
        task_func(data)