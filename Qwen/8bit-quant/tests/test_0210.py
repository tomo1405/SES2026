import pytest
from src_0210 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Mock data
    data = [(1, 2), (3, 4), (5, 6)]
    
    # Call the function
    ax = task_func(data)
    
    # Check if the plot has the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot (data and max tuple)."
    
    # Check if the max tuple is correctly highlighted
    scatter = ax.collections[0]
    points = scatter.get_offsets()
    max_point = np.array([5, 6])
    assert np.allclose(points[-1], max_point), "The max tuple should be the last point in the scatter plot."
    
    # Check if the labels are set correctly
    assert ax.get_xlabel() == 'x', "X-axis label should be 'x'."
    assert ax.get_ylabel() == 'y', "Y-axis label should be 'y'."
    assert ax.get_title() == 'Max Tuple Highlighted', "Title should be 'Max Tuple Highlighted'."
    
    # Check if the legend is present
    legend = ax.get_legend()
    assert legend is not None, "Legend should be present."
    handles, labels = legend.get_legend_handles_labels()
    assert 'Data' in labels, "Legend should include 'Data'."
    assert 'Max Tuple' in labels, "Legend should include 'Max Tuple'."
    
    # Close the plot to avoid display issues in CI/CD environments
    plt.close(fig)

# Run the test
if __name__ == "__main__":
    pytest.main()