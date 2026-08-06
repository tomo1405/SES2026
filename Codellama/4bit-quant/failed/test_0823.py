import pytest
from src_0823 import task_func

def test_task_func():
    # Test that the function raises a ValueError when length is <= 0
    with pytest.raises(ValueError):
        task_func(0, 1)

    # Test that the function raises a ValueError when num_digits is not between 0 and length
    with pytest.raises(ValueError):
        task_func(10, 11)

    # Test that the function returns a string of the correct length
    assert len(task_func(10, 2)) == 10

    # Test that the function returns a string with the correct number of digits
    assert sum(c in string.digits for c in task_func(10, 2)) == 2

    # Test that the function returns a string with the correct number of letters
    assert sum(c in string.ascii_letters for c in task_func(10, 2)) == 8

    # Test that the function returns a string with the correct number of unique characters
    assert len(set(task_func(10, 2))) == 10