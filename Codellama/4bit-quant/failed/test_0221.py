import pytest
from src_0221 import task_func

def test_task_func():
    # Test that the function returns None
    assert task_func(["red", "blue", "green"]) is None

    # Test that the function raises a ValueError when the input is not a list
    with pytest.raises(ValueError):
        task_func(123)

    # Test that the function raises a ValueError when the input is an empty list
    with pytest.raises(ValueError):
        task_func([])

    # Test that the function raises a ValueError when the input contains invalid colors
    with pytest.raises(ValueError):
        task_func(["red", "blue", "green", "yellow"])

    # Test that the function raises a ValueError when the input contains duplicate colors
    with pytest.raises(ValueError):
        task_func(["red", "blue", "green", "red"])