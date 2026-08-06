import pytest
from src_0664 import task_func


def test_task_func():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 8, 16, 32]
    labels = ['data1', 'data2']

    with pytest.raises(ValueError):
        task_func([], [], [])

    fig = task_func(x, y, labels)
    assert fig is not None