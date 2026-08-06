import string

import pytest
from src_0795 import task_func


def test_task_func():
    # Test case 1: Default behavior
    result = task_func(10)
    assert isinstance(result, str)
    assert len(result) == 10
    for char in result:
        assert char in string.ascii_lowercase + BRACKETS

    # Test case 2: Custom length and random seed
    result = task_func(5, random_seed=42)
    assert isinstance(result, str)
    assert len(result) == 5
    for char in result:
        assert char in string.ascii_lowercase + BRACKETS

    # Test case 3: Zero length
    result = task_func(0)
    assert isinstance(result, str)
    assert len(result) == 0

    # Test case 4: Negative length
    with pytest.raises(ValueError):
        task_func(-1)