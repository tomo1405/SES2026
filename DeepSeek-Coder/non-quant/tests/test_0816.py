import pytest
from src_0816 import task_func
import pandas as pd
import numpy as np

# Test cases for the function
def test_task_func():
    # Test case 1: Basic functionality
    data = {'Student': [1, 2, 3], 'Score': [85, 90, 78]}
    test_scores = pd.DataFrame(data)
    result = task_func(test_scores=test_scores, student=1)
    assert result == ([87.67, 7.56], test_scores)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()