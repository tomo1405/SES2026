import pytest
from src_0268 import task_func
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Test that the function returns a tuple with two elements
    data = {'a': 1, 'b': 2, 'c': 3}
    fft, ax = task_func(data)
    assert isinstance(fft, np.ndarray)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Test that the function generates a signal based on the values in `data`
    data = {'a': 1, 'b': 2, 'c': 3}
    signal = np.array(list(data.values()))
    time = np.linspace(0, 2, 2 * 8000, False)
    expected_signal = np.sin(np.outer(time, signal) * np.pi)
    fft, ax = task_func(data)
    assert np.allclose(fft, expected_signal)

    # Test case 3: Test that the function performs a Fast Fourier Transform (FFT) on the signal
    data = {'a': 1, 'b': 2, 'c': 3}
    signal = np.array(list(data.values()))
    time = np.linspace(0, 2, 2 * 8000, False)
    expected_fft = fftpack.fft(signal)
    fft, ax = task_func(data)
    assert np.allclose(fft, expected_fft)

    # Test case 4: Test that the function plots the FFT
    data = {'a': 1, 'b': 2, 'c': 3}
    fft, ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'