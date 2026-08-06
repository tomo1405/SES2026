import pytest
from src_0268 import task_func
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def test_task_func():
    # Mock data input
    data = {'b': 2, 'c': 3}
    sample_rate = 8000
    
    # Call the function
    fft_result, ax = task_func(data, sample_rate)
    
    # Check that the new key 'a' is added to the data
    assert 'a' in data
    assert data['a'] == 1
    
    # Check that the signal is generated correctly
    signal = np.array([1, 2, 3])
    time = np.linspace(0, 2, 2 * sample_rate, False)
    expected_signal = np.sin(np.outer(time, signal) * np.pi)
    assert np.allclose(expected_signal, np.array(list(data.values())))
    
    # Check that the FFT is performed correctly
    expected_fft = fftpack.fft(expected_signal)
    assert np.allclose(fft_result, expected_fft)
    
    # Check that the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'

# To run the tests, you can use the following command in your terminal:
# pytest -v