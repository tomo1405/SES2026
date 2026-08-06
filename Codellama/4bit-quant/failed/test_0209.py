import pytest
from src_0209 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func(10)
    assert len(result) == 2
    
    # Test that the first element is a dictionary
    descriptive_stats, _ = result
    assert isinstance(descriptive_stats, dict)
    
    # Test that the second element is a matplotlib Axes object
    _, ax = result
    assert isinstance(ax, matplotlib.axes.Axes)
    
    # Test that the function raises a ValueError when the input is not a positive integer
    with pytest.raises(ValueError):
        task_func(0)
    
    # Test that the function raises a ValueError when the input is not an integer
    with pytest.raises(ValueError):
        task_func(1.5)