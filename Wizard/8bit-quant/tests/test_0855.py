python
import pytest
from src_0855 import task_func

def test_task_func():
    # Test case 1: valid input
    assert task_func([1, 2, 3]) == ([1, 3, 6], [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

    # Test case 2: invalid input type
    with pytest.raises(TypeError):
        task_func("1, 2, 3")

    # Test case 3: invalid input value
    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

    # Test case 4: empty input
    assert task_func([]) == ([], [])