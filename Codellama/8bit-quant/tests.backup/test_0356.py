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

    # Test the wave
    assert np.allclose(wave, amplitude * np.exp(1j * 2 * math.pi * frequency * time))

    # Test the window
    assert np.allclose(window, get_window('hann', time.size))

    # Test the plot
    assert np.allclose(ax.get_xlabel(), "Time")
    assert np.allclose(ax.get_ylabel(), "Amplitude")
    assert np.allclose(ax.get_title(), "Complex Wave with Hann Window")
    assert np.allclose(ax.get_legend(), "Real Part")
    assert np.allclose(ax.get_legend(), "Imaginary Part")

    return wave, fig, ax