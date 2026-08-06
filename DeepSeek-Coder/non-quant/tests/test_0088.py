import pytest
from src_0088 import task_func
import pandas as pd
from random import choices, seed

# Define test cases
def test_task_func():
    # Test case 1
    products = ["Product A", "Product B", "Product C"]
    ratings = [1, 2, 3]
    weights = [0.2, 0.3, 0.5]
    expected_df = pd.DataFrame({
        "Product": ["Product C", "Product B", "Product A"],
        "Rating": [3, 2, 1]
    })
    
    result_df = task_func(products, ratings, weights)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()