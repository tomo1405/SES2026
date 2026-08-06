import pytest
from src_0202 import task_func
import pandas as pd
import numpy as np

# Create a sample DataFrame for testing
data = {
    'column1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'column2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

def test_task_func():
    # Test case 1: Valid input
    result = task_func(df, 'column1', 5)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 3, "The result should contain 3 elements"
    assert all(isinstance(x, (int, float)) for x in result), "All elements in the result should be numbers"

    # Test case 2: Invalid column
    with pytest.raises(ValueError):
        task_func(df, 'non_existent_column', 5)

    # Test case 3: Invalid value type
    with pytest.raises(ValueError):
        task_func(df, 'column1', 'not_a_number')

    # Add more test cases as needed

# You can add more test cases to cover different scenarios