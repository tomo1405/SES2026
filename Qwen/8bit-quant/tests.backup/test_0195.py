import pytest
from src_0195 import task_func
import numpy as np

def test_task_func():
    # Test with a small data size
    data_size = 10
    data, color = task_func(data_size)
    
    # Check that data is a numpy array of the correct size
    assert isinstance(data, np.ndarray)
    assert data.size == data_size
    
    # Check that data is normally distributed
    assert np.isclose(np.mean(data), 0, atol=0.1)
    assert np.isclose(np.std(data), 1, atol=0.1)
    
    # Check that color is one of the allowed colors
    assert color in BAR_COLOR
    
    # Test with a larger data size
    data_size = 100
    data, color = task_func(data_size)
    
    # Check that data is a numpy array of the correct size
    assert isinstance(data, np.ndarray)
    assert data.size == data_size
    
    # Check that data is normally distributed
    assert np.isclose(np.mean(data), 0, atol=0.1)
    assert np.isclose(np.std(data), 1, atol=0.1)
    
    # Check that color is one of the allowed colors
    assert color in BAR_COLOR