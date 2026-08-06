import pytest
from src_0896 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    
    assert isinstance(array, np.ndarray), "The array should be a numpy array"
    assert len(array) == 10000, "The array should have 10000 elements"
    
    assert isinstance(mean, (int, float)), "The mean should be a number"
    assert isinstance(std, (int, float)), "The standard deviation should be a number"
    
    assert isinstance(ax, plt.Axes), "The ax should be a matplotlib Axes object"
    
    assert len(ax.patches) > 0, "The histogram should have at least one bar"

    plt.close()