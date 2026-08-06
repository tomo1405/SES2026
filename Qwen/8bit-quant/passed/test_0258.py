import pytest
from src_0258 import task_func
import matplotlib.pyplot as plt
import numpy as np
import math

def test_task_func():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 1)

    # Check if the plot has been added correctly
    lines = result_ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line in the plot."

    # Check if the line data is correct
    theta, r = lines[0].get_data()
    expected_r = np.linspace(0, 2 * math.pi, 1000)
    expected_theta = expected_r
    np.testing.assert_array_almost_equal(r, expected_r)
    np.testing.assert_array_almost_equal(theta, expected_theta)

    # Check if the radial label position is set correctly
    rlabel_position = result_ax.get_rlabel_position()
    assert rlabel_position == 45, "The radial label position should be 45 degrees."

    plt.close(fig)