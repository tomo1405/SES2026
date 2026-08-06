import pytest
from src_0895 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Capture the output of task_func
    array, mean, std, ax = task_func()

    # Check that the array is of the correct size
    assert len(array) == 10000, "Array size is incorrect"

    # Check that the mean and standard deviation are calculated correctly
    calculated_mean = np.mean(array)
    calculated_std = np.std(array)
    assert np.isclose(mean, calculated_mean), "Mean calculation is incorrect"
    assert np.isclose(std, calculated_std), "Standard deviation calculation is incorrect"

    # Check that the histogram plot has the correct title and labels
    assert ax.get_title() == 'Histogram of Random Integers', "Plot title is incorrect"
    assert ax.get_xlabel() == 'Value', "X-axis label is incorrect"
    assert ax.get_ylabel() == 'Frequency', "Y-axis label is incorrect"

    # Check that the vertical lines are drawn at the correct positions
    lines = ax.get_lines()
    assert len(lines) == 3, "There should be 3 vertical lines on the plot"
    assert np.isclose(lines[0].get_xdata()[0], mean), "Mean line is not at the correct position"
    assert np.isclose(lines[1].get_xdata()[0], mean + std), "Mean + Std line is not at the correct position"
    assert np.isclose(lines[2].get_xdata()[0], mean - std), "Mean - Std line is not at the correct position"

    # Check that the legend is correct
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == ["Mean", "Standard Deviation"], "Legend labels are incorrect"