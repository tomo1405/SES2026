import pytest
from src_0664 import task_func

def test_task_func():
    x = [1, 2, 3, 4, 5]
    y = [10, 5, 3, 2, 1]
    labels = ['data1', 'data2']

    with pytest.raises(ValueError):
        task_func([], y, labels)
    with pytest.raises(ValueError):
        task_func(x, [], labels)
    with pytest.raises(ValueError):
        task_func(x, y, [])

    fig = task_func(x, y, labels)
    assert fig is not None