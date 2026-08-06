python
import pytest
from src_0125 import task_func

def test_task_func():
    # Test case 1: Valid input
    my_list = [1, 2, 3, 4, 5]
    size = 100
    seed = 100
    expected_time = 0.0
    expected_ax = None
    actual_time, actual_ax = task_func(my_list, size, seed)
    assert actual_time == expected_time
    assert actual_ax == expected_ax

    # Test case 2: Invalid input (not a list)
    my_list = 123
    size = 100
    seed = 100
    with pytest.raises(TypeError):
        task_func(my_list, size, seed)

    # Test case 3: Invalid input (not all elements are numbers)
    my_list = [1, 2, 3, '4', 5]
    size = 100
    seed = 100
    with pytest.raises(ValueError):
        task_func(my_list, size, seed)

    # Test case 4: Invalid input (size is greater than the sum of the list)
    my_list = [1, 2, 3, 4, 5]
    size = 1000
    seed = 100
    with pytest.raises(ValueError):
        task_func(my_list, size, seed)