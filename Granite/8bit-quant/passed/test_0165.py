import pytest
from src_0165 import task_func

def test_task_func():
    # Test case 1: Default arguments
    fig = task_func()
    assert fig is not None

    # Test case 2: Custom arguments
    fig = task_func(num_labels=10, data_range=(0, 100))
    assert fig is not None

    # Test case 3: Invalid argument
    with pytest.raises(ValueError):
        fig = task_func(num_labels=-1)