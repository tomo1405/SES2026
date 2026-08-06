import pandas as pd
import numpy as np
from src_0865 import task_func
import pytest

@pytest.mark.parametrize("fruit_data, expected_output", [
    (
        [("apple", 10), ("banana", 20), ("apple", 15)],
        pd.DataFrame({"Total Count": [25], "Average Count": [25]})
    ),
    (
        [("apple", 10), ("banana", 20), ("orange", 15)],
        pd.DataFrame({"Total Count": [35], "Average Count": [11.666666666666666]})
    ),
    (
        [],
        pd.DataFrame()
    )
])
def test_task_func(fruit_data, expected_output):
    actual_output = task_func(fruit_data)
    pd.testing.assert_frame_equal(actual_output, expected_output)