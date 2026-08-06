import pytest
from src_0795 import task_func

def test_task_func():
    # Test case 1: length = 5, random_seed = 1
    result = task_func(5, random_seed=1)
    assert len(result) == 5
    assert all(c in string.ascii_lowercase + "(){}[]" for c in result)

    # Test case 2: length = 10, random_seed = 2
    result = task_func(10, random_seed=2)
    assert len(result) == 10
    assert all(c in string.ascii_lowercase + "(){}[]" for c in result)

    # Test case 3: length = 0, random_seed = 3
    result = task_func(0, random_seed=3)
    assert len(result) == 0
    assert all(c in string.ascii_lowercase + "(){}[]" for c in result)

    # Test case 4: length = 100, random_seed = 4
    result = task_func(100, random_seed=4)
    assert len(result) == 100
    assert all(c in string.ascii_lowercase + "(){}[]" for c in result)