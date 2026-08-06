import pytest
from src_0919 import task_func
import pandas as pd
import re

# Define test cases
def test_task_func():
    # Test case 1
    data = {'A': ['FOO123', 'BAR456'], 'B': ['BAZ789', 'QUX012']}
    mapping = {'FOO': 'FOO', 'BAR': 'BAR', 'BAZ': 'BAZ', 'QUX': 'QUX'}
    expected_output = pd.DataFrame({'A': ['FOO', 'BAR'], 'B': ['BAZ', 'QUX']})
    result = task_func(data, mapping)
    pd.testing.assert_frame_equal(result, expected_output)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()