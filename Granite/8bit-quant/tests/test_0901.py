import pytest
from src_0901 import task_func


def test_task_func_valid_input():
    input_data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9}
    ]
    expected_output = {
        'x': {
            'mean': 5,
            'sum': 15,
            'max': 7,
            'min': 4,
            'std': 2.1602468994692868
        },
        'y': {
            'mean': 5.333333333333333,
            'sum': 16,
            'max': 8,
            'min': 5,
            'std': 2.1602468994692868
        },
        'z': {
            'mean': 6,
            'sum': 18,
            'max': 9,
            'min': 3,
            'std': 2.1602468994692868
        }
    }
    assert task_func(input_data) == expected_output

def test_task_func_invalid_input():
    input_data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9},
        {'x': 'a', 'y': 'b', 'z': 'c'}
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(input_data)
    assert str(exc_info.value) == "Input must be a list of dictionaries."

def test_task_func_empty_input():
    input_data = []
    expected_output = {
        'x': None,
        'y': None,
        'z': None
    }
    assert task_func(input_data) == expected_output