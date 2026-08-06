import pytest
from src_1065 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func(sample_array):
    fig, ax = plt.subplots()
    result_ax = task_func(sample_array)
    
    # Check if the returned axis is the same as the one created
    assert result_ax == ax
    
    # Check if the title is set correctly
    assert result_ax.get_title() == "Heatmap of the 2D Array"
    
    # Check if the annotations are enabled
    assert result_ax.collections[0].get_array().size > 0
    
    # Check if vmin and vmax are set correctly
    expected_vmin = np.min(sample_array)
    expected_vmax = np.max(sample_array)
    assert result_ax.collections[0].get_clim()[0] == expected_vmin
    assert result_ax.collections[0].get_clim()[1] == expected_vmax

    # Clean up the plot
    plt.close(fig)