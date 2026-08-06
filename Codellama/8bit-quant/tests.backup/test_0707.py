import pytest
from src_0707 import task_func

def test_task_func():
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    columns = ['a', 'b', 'c', 'd', 'e']
    target_column = 'e'

    accuracy = task_func(data, columns, target_column)

    assert accuracy > 0.5