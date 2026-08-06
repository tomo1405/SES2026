import pytest
from src_0247 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func():
    # Test with valid input
    n_waves = 3
    result = task_func(n_waves=n_waves)
    assert isinstance(result, tuple), "The result should be a tuple"
    sine_wave_series, fft_data, ax = result
    assert isinstance(sine_wave_series, list), "sine_wave_series should be a list"
    assert isinstance(fft_data, np.ndarray), "fft_data should be a numpy array"
    assert ax is None, "ax should be None"

    # Add more assertions as needed to cover different scenarios

    # Add more tests as needed