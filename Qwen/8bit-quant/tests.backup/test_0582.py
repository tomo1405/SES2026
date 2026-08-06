import pytest
from src_0582 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    ax = task_func()
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

def test_task_func_plot_data():
    ax = task_func()
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line plotted"
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == SIZE, f"The length of xdata should be {SIZE}"
    assert len(ydata) == SIZE, f"The length of ydata should be {SIZE}"

def test_task_func_default_parameters():
    ax = task_func()
    xdata, _ = ax.get_lines()[0].get_data()
    assert np.array_equal(xdata, np.arange(0, SIZE)), "x_values should be np.arange(0, SIZE)"

def test_task_func_custom_size():
    custom_size = 500
    ax = task_func(size=custom_size)
    xdata, _ = ax.get_lines()[0].get_data()
    assert np.array_equal(xdata, np.arange(0, custom_size)), f"x_values should be np.arange(0, {custom_size})"

def test_task_func_custom_frequency():
    custom_frequency = 3
    ax = task_func(frequency=custom_frequency)
    _, ydata = ax.get_lines()[0].get_data()
    # Check that ydata contains values with the expected frequency
    expected_ydata = [np.sin((2 * np.pi / RANGE) * (x + int(RANGE * random.random()) * custom_frequency)) for x in range(SIZE)]
    assert np.allclose(ydata, expected_ydata), "ydata does not match the expected values with custom frequency"

def test_task_func_no_plot_show():
    with pytest.raises(AssertionError):
        plt.show()  # Ensure plt.show() is not called within the function