import pytest
from src_0768 import task_func

def test_task_func():
    # Test case 1: empty list
    assert task_func([]) == {}

    # Test case 2: single list
    assert task_func([[1, 2, 3]]) == {1: 1, 2: 1, 3: 1}

    # Test case 3: multiple lists
    assert task_func([[1, 2, 3], [4, 5, 6]]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

    # Test case 4: duplicate elements
    assert task_func([[1, 2, 3], [4, 5, 6], [1, 2, 3]]) == {1: 2, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1}

    # Test case 5: invalid input
    with pytest.raises(TypeError):
        task_func(1)

    # Test case 6: invalid input
    with pytest.raises(TypeError):
        task_func([1, 2, 3, "a"])