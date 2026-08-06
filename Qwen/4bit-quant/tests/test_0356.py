import pytest
from src_0356 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    amplitude = 1.0
    frequency = 5.0
    time = np.linspace(0, 1, 100)

    wave, fig, ax = task_func(amplitude, frequency, time)

    # Check the shape of the wave
    assert wave.shape == (100,), "The wave should have the same length as the time array."

    # Check the type of the wave
    assert isinstance(wave, np.ndarray), "The wave should be a numpy array."

    # Check the type of the figure and axis
    assert isinstance(fig, plt.Figure), "The figure should be a matplotlib Figure object."
    assert isinstance(ax, plt.Axes), "The axis should be a matplotlib Axes object."

    # Check the plot labels
    assert ax.get_title() == "Complex Wave with Hann Window", "The plot title is incorrect."
    assert ax.get_xlabel() == "Time", "The x-axis label is incorrect."
    assert ax.get_ylabel() == "Amplitude", "The y-axis label is incorrect."
    assert ax.get_legend().get_texts()[0].get_text() == "Real Part", "The first legend entry is incorrect."
    assert ax.get_legend().get_texts()[1].get_text() == "Imaginary Part", "The second legend entry is incorrect."

    # Close the plot to avoid displaying it during tests
    plt.close(fig)