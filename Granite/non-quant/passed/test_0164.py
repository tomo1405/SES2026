import pytest
from src_0164 import task_func

def test_task_func():
    # Test with valid input
    ax = task_func(rows=5, cols=5)
    assert ax is not None

    # Test with invalid input (cols > len(categories))
    with pytest.raises(ValueError):
        task_func(rows=5, cols=10)