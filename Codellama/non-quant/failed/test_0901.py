import pytest
from src_0901 import task_func

def test_task_func():
    # Test case 1: input is a list of dictionaries
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_output = {'x': {'mean': 2.5, 'sum': 10, 'max': 4, 'min': 1, 'std': 1.5811388300841898},
                      'y': {'mean': 3.5, 'sum': 12, 'max': 5, 'min': 2, 'std': 1.5811388300841898},
                      'z': {'mean': 4.5, 'sum': 18, 'max': 6, 'min': 3, 'std': 1.5811388300841898}}
    assert task_func(d) == expected_output

    # Test case 2: input is an empty list
    d = []
    expected_output = {'x': None, 'y': None, 'z': None}
    assert task_func(d) == expected_output

    # Test case 3: input is not a list
    d = 'not a list'
    with pytest.raises(ValueError):
        task_func(d)

    # Test case 4: input is a list with non-dict elements
    d = [{'x': 1, 'y': 2, 'z': 3}, 'not a dict']
    with pytest.raises(ValueError):
        task_func(d)