import pytest
from src_0992 import task_func

def test_task_func():
    # Test case 1: length = 10
    result = task_func(10)
    assert isinstance(result, str)
    assert len(result) >= 10

    # Test case 2: length = 0
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 3: length = -1
    with pytest.raises(ValueError):
        task_func(-1)

    # Test case 4: length = 1000
    result = task_func(1000)
    assert isinstance(result, str)
    assert len(result) >= 1000