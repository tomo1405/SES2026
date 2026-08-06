python
import pytest
from src_0901 import task_func

def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == {'x': None, 'y': None, 'z': None}

    # Test case 2: List with missing values
    assert task_func([{'x': 1, 'y': 2}, {'x': 3, 'z': 4}]) == {'x': {'mean': 2.0, 'sum': 4.0, 'max': 3.0, 'min': 1.0, 'std': 1.0}, 'y': {'mean': 2.0, 'sum': 2.0, 'max': 2.0, 'min': 2.0, 'std': 0.0}, 'z': {'mean': 4.0, 'sum': 4.0, 'max': 4.0, 'min': 4.0, 'std': 0.0}}

    # Test case 3: List with invalid input type
    with pytest.raises(ValueError):
        task_func('not a list')

    # Test case 4: List with invalid dictionary type
    with pytest.raises(ValueError):
        task_func([{'x': 1, 'y': 2}, 'not a dictionary'])