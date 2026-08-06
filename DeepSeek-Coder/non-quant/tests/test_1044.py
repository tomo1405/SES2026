import pytest
from src_1044 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Define test cases
def test_task_func():
    # Test case 1: Normal case
    data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    result = task_func(data_list=data_list)
    assert result is not None

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()