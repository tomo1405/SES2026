import math

import matplotlib.pyplot as plt
import numpy as np
from src_0356 import task_func


def test_task_func():
    amplitude = 10
    frequency = 100
    time = np.linspace(0, 1, 1000)
    wave, fig, ax = task_func(amplitude, frequency, time)

    # Test the wave
    assert np.allclose(wave, amplitude * np.exp(1j * 2 * math.pi * frequency * time))

    # Test the window
    assert np.allclose(wave * window, amplitude * np.exp(1j * 2 * math.pi * frequency * time))

    # Test the plot
    assert fig.axes[0].get_title() == "Complex Wave with Hann Window"
    assert fig.axes[0].get_xlabel() == "Time"
    assert fig.axes[0].get_ylabel() == "Amplitude"
    assert fig.axes[0].get_legend() == "Real Part"
    assert fig.axes[1].get_legend() == "Imaginary Part"

    # Test the return values
    assert isinstance(wave, np.ndarray)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)