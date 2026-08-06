import pytest
from src_0356 import task_func
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def test_task_func():
    amplitude = 10
    frequency = 100
    time = np.linspace(0, 1, 1000)
    wave, fig, ax = task_func(amplitude, frequency, time)

    # Test that the wave is a complex numpy array
    assert isinstance(wave, np.ndarray)
    assert wave.dtype == np.complex128

    # Test that the wave has the correct shape
    assert wave.shape == (1000,)

    # Test that the wave has the correct values
    expected_wave = amplitude * np.exp(1j * 2 * math.pi * frequency * time)
    np.testing.assert_allclose(wave, expected_wave)

    # Test that the window is applied correctly
    window = get_window('hann', time.size)
    expected_wave *= window
    np.testing.assert_allclose(wave, expected_wave)

    # Test that the plot is created correctly
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Complex Wave with Hann Window"
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Amplitude"
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == "Real Part"
    assert ax.get_lines()[1].get_label() == "Imaginary Part"