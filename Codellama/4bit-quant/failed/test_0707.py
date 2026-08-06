import pytest
from src_0707 import task_func

def test_task_func():
    data = {'col1': [1, 2, 3, 4, 5], 'col2': [2, 4, 6, 8, 10], 'target': [0, 1, 1, 0, 1]}
    columns = ['col1', 'col2']
    target_column = 'target'

    accuracy = task_func(data, columns, target_column)

    assert accuracy > 0.5