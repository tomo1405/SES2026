import pytest
from src_0268 import task_func
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import io
import sys

# Redirect stdout to capture plot output
sys.stdout = io.StringIO()

def test_task_func_output():
    data = {'b': 2, 'c': 3}
    sample_rate = 8000
    fft, ax = task_func(data, sample_rate)

    # Check if the 'a' key is added to the data dictionary
    assert 'a' in data and data['a'] == 1

    # Check if the signal array has the correct shape
    signal = np.array(list(data.values()))
    expected_signal_shape = (2 * sample_rate, len(signal))
    assert signal.shape == (len(signal),)
    assert fft.shape == expected_signal_shape

    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'

    # Restore stdout
    sys.stdout = sys.__stdout__

# Run the test
if __name__ == "__main__":
    pytest.main()