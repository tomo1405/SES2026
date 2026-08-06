import pytest
from src_1002 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

# Mock data to simulate CSV file content
csv_data = """column1
1
2
3
4
5"""

@pytest.fixture
def csv_file():
    return io.StringIO(csv_data)

def test_task_func(csv_file):
    # Create a temporary file with the mock data
    temp_file = io.StringIO(csv_data)
    
    # Call the function with the path to the temporary file
    ax = task_func(temp_file)
    
    # Check if the returned object is an AxesSubplot instance
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object."
    
    # Check if the plot has been created correctly
    assert len(ax.lines) == 1, "The plot should contain exactly one line."
    
    # Check if the title and labels are set correctly
    assert ax.get_title() == "          Plot Title          :          Normalized Column 1          ", "The plot title is not set correctly."
    assert ax.get_xlabel() == "             Index            :             Normalized Value            ", "The x-axis label is not set correctly."
    assert ax.get_ylabel() == "         Frequency          :         Normalized Value          ", "The y-axis label is not set correctly."

# Run the tests
if __name__ == "__main__":
    pytest.main()