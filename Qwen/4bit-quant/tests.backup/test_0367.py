import pytest
from src_0367 import task_func
import matplotlib.pyplot as plt
import io
import sys

@pytest.fixture
def number_list():
    return [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

@pytest.fixture
def bins():
    return 5

def test_task_func(number_list, bins):
    # Redirect stdout to capture any print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Call the function
    ax = task_func(number_list, bins)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return an AxesSubplot object"
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Histogram', "The plot should have the title 'Histogram'"
    assert ax.get_xlabel() == 'Number', "The plot should have the x-label 'Number'"
    assert ax.get_ylabel() == 'Frequency', "The plot should have the y-label 'Frequency'"
    
    # Check if the plot has the correct number of bins
    n, bins, patches = ax.hist(number_list, bins=bins)
    assert len(bins) == bins + 1, f"The plot should have {bins + 1} bins"

# Run the tests
if __name__ == "__main__":
    pytest.main()