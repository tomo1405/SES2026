import pandas as pd
import numpy as np
from src_0865 import task_func
import pytest

@pytest.mark.parametrize("fruit_data, expected_output", [
    ([], pd.DataFrame()),
    (
        [("apple", 10), ("banana", 20), ("apple", 15)],
        pd.DataFrame({
            "Total Count": [25],
            "Average Count": [25]
        }, index=pd.Index(["apple", "banana"], name="fruits"))
    ),
    (
        [("apple", 10), ("banana", 20), ("apple", 15), ("orange", 5)],
        pd.DataFrame({
            "Total Count": [30],
            "Average Count": [30]
        }, index=pd.Index(["apple", "banana", "orange"], name="fruits"))
    )
])
def test_task_func(fruit_data, expected_output):
    assert task_func(fruit_data).equals(expected_output)