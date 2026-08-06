import pytest
from src_1080 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Sample data
    data = {
        "Price_String": ["1,000", "2,500", "3,000", "4,500", "5,000"]
    }
    
    # Expected results
    expected_mean = 3000.0
    expected_median = 3000.0
    expected_std_dev = np.sqrt(625000 / 4)  # Sample standard deviation

    # Call the function
    result, ax = task_func(data)

    # Check the results
    assert np.isclose(result["mean"], expected_mean), f"Expected mean {expected_mean}, got {result['mean']}"
    assert np.isclose(result["median"], expected_median), f"Expected median {expected_median}, got {result['median']}"
    assert np.isclose(result["std_dev"], expected_std_dev), f"Expected std_dev {expected_std_dev}, got {result['std_dev']}"

    # Check the type of the plot result
    assert isinstance(ax, tuple), "The plot result should be a tuple"

# Run the tests
if __name__ == "__main__":
    pytest.main()