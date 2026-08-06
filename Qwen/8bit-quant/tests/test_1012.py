import pytest
from src_1012 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mock data for testing
csv_data = u"""column1,column2
A,10
A,20
B,30
B,40
C,50"""

@pytest.fixture
def mock_csv_file():
    return io.StringIO(csv_data)

def test_task_func(mock_csv_file):
    # Call the function with the mock CSV file
    ax = task_func(mock_csv_file, col1_name="column1", col2_name="column2")

    # Check if the plot has the correct number of bars
    assert len(ax.patches) == 3  # There should be 3 bars for A, B, and C

    # Check if the plot has the correct title
    assert ax.get_title() == "Mean of column2 Grouped by column1"

    # Check if the plot has the correct x-axis label
    assert ax.get_xlabel() == "column1"

    # Check if the plot has the correct y-axis label
    assert ax.get_ylabel() == "Mean of column2"

    # Check if the plot has the correct data
    expected_means = [15, 35, 50]  # Means for A, B, and C
    for i, bar in enumerate(ax.patches):
        assert bar.get_height() == expected_means[i]

    # Close the plot to avoid memory leaks
    plt.close(ax.figure)