import pytest
from src_0356 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    amplitude = 1.0
    frequency = 1.0
    time = np.linspace(0, 1, 1000)

    wave, fig, ax = task_func(amplitude, frequency, time)

    # Check if wave is a numpy array of complex numbers
    assert isinstance(wave, np.ndarray)
    assert np.iscomplexobj(wave)

    # Check if the shape of the wave matches the input time array
    assert wave.shape == time.shape

    # Check if fig and ax are matplotlib figure and axes objects
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot():
    amplitude = 1.0
    frequency = 1.0
    time = np.linspace(0, 1, 1000)

    _, fig, ax = task_func(amplitude, frequency, time)

    # Check if the plot has the correct labels and title
    assert ax.get_title() == "Complex Wave with Hann Window"
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Amplitude"
    assert "Real Part" in [line.get_label() for line in ax.lines]
    assert "Imaginary Part" in [line.get_label() for line in ax.lines]

    # Close the plot to avoid memory leaks
    plt.close(fig)