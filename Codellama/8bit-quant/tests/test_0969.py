import pytest
import seaborn as sns
from src_0969 import task_func


def test_task_func_valid_input():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ax = task_func(data)
    assert isinstance(ax, sns.heatmap)

def test_task_func_invalid_input():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    with pytest.raises(ValueError):
        task_func(data)