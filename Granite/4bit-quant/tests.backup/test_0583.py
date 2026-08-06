import pytest
from src_0583 import task_func

def test_task_func():
    # Test case 1: Default size
    fig = task_func()
    assert fig is not None
    assert isinstance(fig, object)
    
    # Test case 2: Custom size
    fig = task_func(size=2000)
    assert fig is not None
    assert isinstance(fig, object)
    
    # Test case 3: Invalid size
    with pytest.raises(ValueError):
        task_func(size=-100)