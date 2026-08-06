import pytest
from src_0268 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Prepare test data
    data = {'b': 2, 'c': 3}
    sample_rate = 8000
    
    # Call the function
    fft_result, ax = task_func(data, sample_rate)
    
    # Check the type of the returned values
    assert isinstance(fft_result, np.ndarray), "The first return value should be a NumPy array"
    assert isinstance(ax, plt.Axes), "The second return value should be a Matplotlib Axes object"
    
    # Check the shape of the FFT result
    expected_shape = (2 * sample_rate, len(data) + 1)
    assert fft_result.shape == expected_shape, f"FFT result shape is incorrect. Expected {expected_shape}, got {fft_result.shape}"
    
    # Check that the key 'a' has been added to the data
    assert 'a' in data and data['a'] == 1, "Key 'a' with value 1 should be added to the input data"

# Run the tests
if __name__ == "__main__":
    pytest.main()