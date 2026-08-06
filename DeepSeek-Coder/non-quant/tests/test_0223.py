import pytest
from src_0223 import task_func
import numpy as np
import matplotlib.pyplot as plt
import math

@pytest.fixture
def example_input():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def test_task_func(example_input):
    result, _ = task_func(example_input)
    assert isinstance(result, list), "The result should be a list"
    assert all(isinstance(x, (int, float)) for x in result), "All elements should be numbers"
    assert len(result) == len(example_input), "The length of the result should be the same as the input"

def test_plot(example_input):
    result, ax = task_func(example_input)
    assert ax is not None, "The plot should be created"
    assert isinstance(ax, plt.Axes), "The plot should be created"
    assert ax.get_title() == "Cumulative Sum Plot", "The plot should have the correct title"
    assert ax.get_xlabel() == "Index", "The x-axis label should be 'Index'"
    assert ax.get_ylabel() == "Cumulative Sum", "The y-axis label should be 'Cumulative Sum'"

pytest.main()