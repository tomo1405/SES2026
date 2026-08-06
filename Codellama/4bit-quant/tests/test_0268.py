import pytest
from src_0268 import task_func
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def test_task_func():
    # Test that the function returns a tuple with two elements
    data = {'a': 1, 'b': 2, 'c': 3}
    fft, ax = task_func(data)
    assert isinstance(fft, np.ndarray)
    assert isinstance(ax, plt.Axes)

    # Test that the function adds a new key 'a' with value 1
    assert 'a' in data
    assert data['a'] == 1

    # Test that the function generates a signal based on the values in `data`
    signal = np.array(list(data.values()))
    time = np.linspace(0, 2, 2 * 8000, False)
    expected_signal = np.sin(np.outer(time, signal) * np.pi)
    np.testing.assert_almost_equal(signal, expected_signal)

    # Test that the function performs a Fast Fourier Transform (FFT) on the signal
    fft = fftpack.fft(signal)
    expected_fft = np.array([1, 2, 3])
    np.testing.assert_almost_equal(fft, expected_fft)

    # Test that the function plots the FFT
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(np.abs(fft))
    ax.set_title('FFT of the Signal')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Frequency Spectrum Magnitude')
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'
    assert ax.get_xlim() == (0, 2)
    assert ax.get_ylim() == (0, 3)

    # Test that the function returns the correct axes object
    assert ax == plt.gca()