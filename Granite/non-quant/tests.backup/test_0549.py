import pytest
from src_0549 import task_func

def test_task_func():
    # Test case 1: Default string length (100)
    result = task_func()
    assert isinstance(result, str)
    assert len(result) == 100

    # Test case 2: Custom string length (50)
    result = task_func(string_length=50)
    assert isinstance(result, str)
    assert len(result) == 50

    # Test case 3: Invalid string length (-1)
    with pytest.raises(ValueError):
        task_func(string_length=-1)

    # Test case 4: Invalid string length (not an integer)
    with pytest.raises(TypeError):
        task_func(string_length='abc')