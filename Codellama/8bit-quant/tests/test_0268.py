import pytest
from src_0268 import task_func
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def test_task_func():
    # Test that the function returns the correct type
    assert isinstance(task_func(data={'a': 1, 'b': 2, 'c': 3}, sample_rate=8000), tuple)

    # Test that the function returns the correct values
    fft, ax = task_func(data={'a': 1, 'b': 2, 'c': 3}, sample_rate=8000)
    assert np.allclose(fft, np.array([1, 2, 3]))
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'

    # Test that the function raises an error when the input data is not a dictionary
    with pytest.raises(TypeError):
        task_func(data=[1, 2, 3], sample_rate=8000)

    # Test that the function raises an error when the input data is empty
    with pytest.raises(ValueError):
        task_func(data={}, sample_rate=8000)