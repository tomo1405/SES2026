import numpy as np
import itertools
from src_0873 import task_func
import pytest

# Define a test data list with different lengths
data_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Generate the expected output by manually calculating the mean values
expected_output = [2, 5, 7]

# Define a test case using the pytest.mark.parametrize decorator
@pytest.mark.parametrize("data_list, expected_output", [
    (data_list, expected_output)
])
def test_task_func(data_list, expected_output):
    # Call the function under test
    output = task_func(data_list)

    # Assert that the output matches the expected output
    assert output == expected_output