import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_1037 import task_func


def test_task_func():
    # Create sample series
    s1 = pd.Series(np.random.rand(10), name='Series1')
    s2 = pd.Series(np.random.rand(10), name='Series2')

    # Ensure that there is at least one common element
    s1.iloc[0] = s2.iloc[0]

    # Call the function
    ax, intersection_count = task_func(s1, s2)

    # Check if the intersection count is correct
    assert intersection_count == 1

    # Check if the axes object is created
    assert isinstance(ax, plt.Axes)

    # Check if the plot has the correct title
    assert ax.get_title() == "Overlap Between Series1 and Series2"

    # Check if the plot has the correct x-axis label
    assert ax.get_xlabel() == 'Series1'

    # Check if the plot has the correct y-axis label
    assert ax.get_ylabel() == 'Type'

    # Check if the plot has the correct number of lines (swarm plot + intersection line)
    assert len(ax.lines) == 1  # Only the intersection line, no swarm plot lines in this test

    # Check if the intersection line is at the correct position
    intersection_line = ax.lines[0]
    assert intersection_line.get_xdata()[0] == s1.iloc[0]
    assert intersection_line.get_color() == 'red'
    assert intersection_line.get_linestyle() == '--'