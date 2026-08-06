import pytest
from src_0456 import task_func
import numpy as np
from scipy import stats

def test_task_func():
    # Test with mean=0, std_dev=1, n=1000
    samples = task_func(0, 1, 1000)
    
    # Check that the output is a numpy array
    assert isinstance(samples, np.ndarray)
    
    # Check that the number of samples is correct
    assert len(samples) == 1000
    
    # Check that the mean of the samples is close to the input mean
    assert np.isclose(np.mean(samples), 0, atol=0.1)
    
    # Check that the standard deviation of the samples is close to the input std_dev
    assert np.isclose(np.std(samples), 1, atol=0.1)
    
    # Test with different parameters
    samples = task_func(5, 2, 500)
    
    # Check that the output is a numpy array
    assert isinstance(samples, np.ndarray)
    
    # Check that the number of samples is correct
    assert len(samples) == 500
    
    # Check that the mean of the samples is close to the input mean
    assert np.isclose(np.mean(samples), 5, atol=0.2)
    
    # Check that the standard deviation of the samples is close to the input std_dev
    assert np.isclose(np.std(samples), 2, atol=0.2)