import pytest
from src_0210 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [(1, 2), (3, 4), (5, 6)]

def test_task_func(sample_data):
    ax = task_func(sample_data)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the data points are plotted correctly
    lines = ax.get_lines()
    assert len(lines) == 2  # One line for scatter plot and one for legend
    
    # Check if the max tuple is highlighted correctly
    max_tuple = max(sample_data, key=lambda x: x[1])
    max_point = ax.collections[1].get_offsets()[0]
    assert tuple(max_point) == max_tuple
    
    # Check if labels and title are set correctly
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Max Tuple Highlighted'
    
    # Check if legend is present
    assert len(ax.get_legend().get_texts()) == 2

# Run the tests
if __name__ == "__main__":
    pytest.main()