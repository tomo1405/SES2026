import pytest
from src_1080 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Sample data
    data = {
        "Price_String": ["1,000", "2,500", "3,000", "4,000", "5,000"]
    }
    
    # Expected results
    expected_mean = 3000.0
    expected_median = 3000.0
    expected_std_dev = np.std([1000, 2500, 3000, 4000, 5000], ddof=1)
    
    # Call the function
    result, ax = task_func(data)
    
    # Check if the results match the expected values
    assert np.isclose(result["mean"], expected_mean), f"Mean is incorrect: {result['mean']}"
    assert np.isclose(result["median"], expected_median), f"Median is incorrect: {result['median']}"
    assert np.isclose(result["std_dev"], expected_std_dev), f"Standard deviation is incorrect: {result['std_dev']}"
    
    # Check if the histogram plot was created
    assert isinstance(ax, tuple), "Histogram plot not created correctly"

# Run the test
if __name__ == "__main__":
    pytest.main()