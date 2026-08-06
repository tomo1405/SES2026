import pytest
from src_0530 import task_func
import random
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    result = task_func(num_rolls=100, num_dice=3)
    assert isinstance(result, tuple), "The function should return a tuple."
    sums_counter, _ = result
    assert isinstance(sums_counter, Counter), "The first element of the tuple should be a Counter."
    assert len(sums_counter) > 0, "The Counter should not be empty."

    # Test with plot_path
    result_with_plot = task_func(num_rolls=100, num_dice=2, plot_path="plot.png")
    assert plt.gcf().get_axes() is not None, "The plot should be saved if plot_path is provided."

    # Clean up the plot
    plt.close()