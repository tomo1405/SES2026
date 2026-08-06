import pytest
from src_0901 import task_func

def test_task_func_valid_input():
    # Test with a valid input
    data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6}
    ]
    result = task_func(data)
    assert result == {
        'x': {
            'mean': 2.5,
            'sum': 7,
            'max': 4,
            'min': 1,
            'std': 1.7320508075688772
        },
        'y': {
            'mean': 3.5,
            'sum': 7,
            'max': 6,
            'min': 2,
            'std': 1.7320508075688772
        },
        'z': {
            'mean': 4.5,
            'sum': 9,
            'max': 6,
            'min': 3,
            'std': 1.7320508075688772
        }
    }

def test_task_func_invalid_input():
    # Test with an invalid input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])
    with pytest.raises(ValueError):
        task_func([{'a': 1}, {'b': 2}])

def test_task_func_empty_input():
    # Test with an empty input
    result = task_func([])
    assert result == {
        'x': None,
        'y': None,
        'z': None
    }