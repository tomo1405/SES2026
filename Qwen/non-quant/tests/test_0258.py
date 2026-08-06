import pytest
from src_0258 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup_axes():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    return ax

def test_task_func(setup_axes):
    ax = setup_axes
    num_turns = 3
    result_ax = task_func(ax, num_turns)
    
    # Check if the plot has been added to the axes
    lines = result_ax.get_lines()
    assert len(lines) == 1, "The plot should have exactly one line."
    
    # Check if the data of the plot is correct
    xdata, ydata = lines[0].get_data()
    expected_xdata = np.linspace(0, num_turns * 2 * np.pi, 1000)
    expected_ydata = expected_xdata
    np.testing.assert_array_almost_equal(xdata, expected_xdata)
    np.testing.assert_array_almost_equal(ydata, expected_ydata)
    
    # Check if the rlabel position is set correctly
    assert result_ax.rlabel_position == num_turns * 45, "The rlabel position should be set to num_turns * 45."

# To run the tests, you can use the following command in your terminal:
# pytest <path_to_this_file>