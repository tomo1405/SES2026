python
import pytest
from src_0516 import task_func

def test_task_func_valid_input():
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    df, heatmap = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(heatmap, sns.axisgrid.Grid)

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([
            [1, 2, 3, 4],
            [5, 6, 7, 8, 9],
        ])