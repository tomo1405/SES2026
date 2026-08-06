import pytest
from src_1083 import task_func
import pandas as pd
from scipy.stats import pearsonr

# Define test cases
def test_task_func():
    # Test case 1: Normal case
    data = {
        "Score_String": [1, 2, 3],
        "Grade": ["A", "B", "C"]
    }
    expected_output = pearsonr([1, 2, 3], [0, 1, 2])[0]
    assert task_func(data) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()