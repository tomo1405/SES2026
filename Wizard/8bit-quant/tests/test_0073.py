python
import pytest
from src_0073 import task_func

def test_task_func():
    # Test case 1
    directory = "data"
    df, hist = task_func(directory)
    assert df.shape == (100, 4)
    assert hist is not None

    # Test case 2
    directory = "data_empty"
    df, hist = task_func(directory)
    assert df.shape == (0, 4)
    assert hist is None