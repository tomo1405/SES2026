import pytest
from src_0549 import task_func

def test_task_func():
    # Test with default string length
    result = task_func()
    assert isinstance(result, str)
    assert len(result) == 100

    # Test with custom string length
    result = task_func(string_length=50)
    assert isinstance(result, str)
    assert len(result) == 50

    # Test with invalid string length
    with pytest.raises(ValueError):
        task_func(string_length=-1)