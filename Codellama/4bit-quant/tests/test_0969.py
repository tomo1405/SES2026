import pytest
from src_0969 import task_func

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ax = task_func(data)
    assert ax.get_title() == "Cumulative Sum"
    assert ax.get_xlabel() == "Columns"
    assert ax.get_ylabel() == "Rows"
    assert ax.get_yticks() == [0, 1, 2]
    assert ax.get_xticks() == [0, 1, 2]
    assert ax.get_yticklabels() == ["0", "1", "2"]
    assert ax.get_xticklabels() == ["0", "1", "2"]
    assert ax.get_data() == [
        [0, 1, 3],
        [0, 2, 6],
        [0, 3, 9]
    ]