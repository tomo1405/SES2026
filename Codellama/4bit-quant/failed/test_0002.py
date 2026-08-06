import pytest
from src_0002 import task_func

def test_task_func():
    # Test that the function returns a dictionary
    assert isinstance(task_func(), dict)

    # Test that the function raises a ValueError when length is negative
    with pytest.raises(ValueError):
        task_func(-1)

    # Test that the function returns a dictionary with the correct keys
    result = task_func()
    assert set(result.keys()) == set(string.ascii_uppercase + string.ascii_lowercase)

    # Test that the function returns the correct values for each key
    for key in result:
        assert result[key] == char_counts[key]