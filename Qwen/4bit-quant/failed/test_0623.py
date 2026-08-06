import pytest
from src_0623 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def sample_data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(sample_data):
    ax = task_func(sample_data)
    
    # Check if the axis object is of the correct type
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."
    
    # Check if the histogram is plotted correctly
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line plot on the axes."
    
    # Check if the title contains the expected format
    title = ax.get_title()
    assert "Fit results: mu =" in title and "std =" in title, "The title should contain 'Fit results: mu =' and 'std ='."
    
    # Check if the histogram data matches the input data
    hist_data, _ = ax.get_legend_handles_labels()
    assert len(hist_data) == 1, "There should be exactly one histogram plot on the axes."
    
    # Check if the plot limits are set correctly
    xmin, xmax = ax.get_xlim()
    assert xmin <= min(chain(*sample_data)) and xmax >= max(chain(*sample_data)), "Plot limits should encompass the data range."

    # Check if the plot is closed after the function execution
    plt.close('all')