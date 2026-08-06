import pytest
from src_0313 import task_func

def test_task_func():
    distribution, ax = task_func()
    
    # Check that the distribution is of the correct size
    assert len(distribution) == 1000
    
    # Check that the distribution is a list of numbers
    assert all(isinstance(x, (int, float)) for x in distribution)
    
    # Check that the ax object is not None
    assert ax is not None
    
    # Check that the number of bins is correct
    assert len(ax.patches) == 30