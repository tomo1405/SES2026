import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Define test cases
def test_task_func():
    # Test data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    columns_to_scale = ['A']

    # Expected output
    expected_output = pd.DataFrame({
        'A': [0.0, 0.25, 0.5, 0.75, 1.0],
        'B': [1.0, 0.75, 0.5, 0.25, 0.0]
    })

    # Call the function
    result = task_func(data, columns_to_scale)

    # Assert the result
    pd.testing.assert_frame_equal(result, expected_output)

# Run the test
if __name__ == "__main__":
    pytest.main()