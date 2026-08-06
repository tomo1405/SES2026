import pytest
from src_0895 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    
    # Check if the array is of the correct size
    assert len(array) == 10000
    
    # Check if the mean is calculated correctly
    assert mean == pytest.approx(np.mean(array), "Mean calculation is incorrect"
    
    # Check if the standard deviation is calculated correctly
    assert std == pytest.approx(np.std(array)), "Standard deviation calculation is incorrect"
    
    # Check if the plot is generated without errors
    assert ax is not None, "Plot generation failed"