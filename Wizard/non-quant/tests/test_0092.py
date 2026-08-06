python
import pytest
from src_0092 import task_func

def test_task_func():
    data = {'x': [1, 2, 3, 4, 5], 'y': [5, 7, 9, 11, 13]}
    column1 = 'x'
    column2 = 'y'
    expected_result = ((1.0, 0.0, 1.0, 0.0, 0.0), None)

    result = task_func(data, column1, column2)

    assert result == expected_result

def test_task_func_invalid_column():
    data = {'x': [1, 2, 3, 4, 5], 'y': [5, 7, 9, 11, 13]}
    column1 = 'a'
    column2 = 'b'

    with pytest.raises(ValueError):
        task_func(data, column1, column2)