import pytest
from src_1080 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return {
        "Price_String": ["1,000", "2,500", "3,750", "4,200", "5,000"]
    }

def test_task_func(sample_data):
    result, ax = task_func(sample_data)
    
    # Check if the result is a dictionary with correct keys
    assert isinstance(result, dict)
    assert set(result.keys()) == {"mean", "median", "std_dev"}
    
    # Check if the values are calculated correctly
    expected_mean = np.mean([1000, 2500, 3750, 4200, 5000])
    expected_median = np.median([1000, 2500, 3750, 4200, 5000])
    expected_std_dev = np.std([1000, 2500, 3750, 4200, 5000], ddof=1)
    
    assert np.isclose(result["mean"], expected_mean)
    assert np.isclose(result["median"], expected_median)
    assert np.isclose(result["std_dev"], expected_std_dev)
    
    # Check if the histogram plot is created correctly
    assert isinstance(ax, tuple)
    assert len(ax) == 2  # ax contains (n, bins, patches)
    assert isinstance(ax[0], np.ndarray)  # n
    assert isinstance(ax[1], np.ndarray)  # bins
    assert isinstance(ax[2], list)  # patches

    # Clean up the plot to avoid interference with other tests
    plt.close()

# Run the tests
if __name__ == "__main__":
    pytest.main()