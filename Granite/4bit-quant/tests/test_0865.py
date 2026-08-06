import pandas as pd
import numpy as np
from src_0865 import task_func
import pytest

@pytest.mark.parametrize("fruit_data, expected_output", [
    (
        [("apple", 10), ("banana", 20), ("apple", 5)],
        pd.DataFrame({"Total Count": [15, 20], "Average Count": [5, 10]})
    ),
    (
        [],
        pd.DataFrame()
    ),
    (
        [("apple", 10), ("banana", 20), ("orange", 15)],
        pd.DataFrame({"Total Count": [10, 20, 15], "Average Count": [5, 10, 5]})
    )
])
def test_task_func(fruit_data, expected_output):
    """
    Test the task_func function with different inputs and expected outputs.
    """
    actual_output = task_func(fruit_data)
    pd.testing.assert_frame_equal(actual_output, expected_output)