import pytest
from src_0065 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define test cases
def test_task_func():
    # Create a sample DataFrame
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [4, 5, 6, 7],
        'col3': [7, 8, 9, 10]
    }
    expected_df = pd.DataFrame({
        'col1': [1, 2, 3, 4],
        'col2': [4, 5, 6, 7],
        'col3': [7, 8, 9, 10]
    })
    expected_analyzed_df = pd.DataFrame({
        'col1': [1, 2, 3, 4],
        'col2': [4, 5, 6, 7],
        'col3': [7, 8, 9, 10]
    })

    # Call the function
    result, _ = task_func(data)

    # Assert the result
    pd.testing.assert_frame_equal(result, expected_analyzed_df)

# Run the tests
if __name__ == "__main__":
    pytest.main()