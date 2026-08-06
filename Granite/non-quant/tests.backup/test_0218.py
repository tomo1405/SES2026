import pytest
from src_0218 import task_func

def test_task_func():
    ax, mean, std = task_func()
    assert ax is not None  # Check if the returned ax is not None
    assert mean is not None  # Check if the returned mean is not None
    assert std is not None  # Check if the returned std is not None