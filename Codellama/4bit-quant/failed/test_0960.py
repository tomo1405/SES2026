import pytest
from src_0960 import task_func

def test_task_func():
    # Test with no seed
    assert task_func("hello") == "hello"
    assert task_func("world") == "world"

    # Test with seed
    assert task_func("hello", seed=123) == "hello"
    assert task_func("world", seed=123) == "world"

    # Test with different seeds
    assert task_func("hello", seed=123) != task_func("hello", seed=456)
    assert task_func("world", seed=123) != task_func("world", seed=456)

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(123)

    with pytest.raises(ValueError):
        task_func(None)