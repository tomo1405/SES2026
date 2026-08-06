import pytest
from src_0664 import task_func


def test_task_func():
    x = [1, 2, 3]
    y = [4, 5, 6]
    labels = ['label1', 'label2', 'label3']

    with pytest.raises(ValueError):
        task_func([], [], [])

    with pytest.raises(ValueError):
        task_func(x, [], [])

    with pytest.raises(ValueError):
        task_func([], y, [])

    with pytest.raises(ValueError):
        task_func(x, y, [])

    with pytest.raises(ValueError):
        task_func([], y, labels)

    with pytest.raises(ValueError):
        task_func(x, [], labels)

    with pytest.raises(ValueError):
        task_func([], y, labels)

    with pytest.raises(ValueError):
        task_func(x, y, [])

    with pytest.raises(ValueError):
        task_func(x, y, labels)

    assert task_func(x, y, labels) is not None