import pytest
from src_0117 import task_func
import numpy as np
import io
import sys

def test_task_func():
    # Redirect stdout to capture plot output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Define test parameters
    mu = 0
    sigma = 1
    sample_size = 1000
    
    # Call the function
    result = task_func(mu, sigma, sample_size)
    
    # Check that the result is a numpy array
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    
    # Check that the array has the correct shape
    assert result.shape == (sample_size,), f"The result should have shape ({sample_size},)"
    
    # Check that the mean of the samples is close to the expected mean
    assert np.isclose(np.mean(result), mu, atol=0.1), "The mean of the samples should be close to the expected mean"
    
    # Check that the standard deviation of the samples is close to the expected standard deviation
    assert np.isclose(np.std(result), sigma, atol=0.1), "The standard deviation of the samples should be close to the expected standard deviation"
    
    # Reset stdout
    sys.stdout = sys.__stdout__

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])