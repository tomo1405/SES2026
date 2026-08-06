import pandas as pd
import numpy as np
from src_0415 import task_func
import pytest

@pytest.mark.parametrize("data, column, expected_output", [
    ({"a": [1, 2, 3], "b": [4, 5, 6]}, "a", (pd.DataFrame({"b": [4, 5, 6]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, "b", (pd.DataFrame({"a": [1, 2, 3], "c": [7, 8, 9]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7.0, 8.0, 9.0]}, "b", (pd.DataFrame({"a": [1, 2, 3], "c": [7.0, 8.0, 9.0]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "b", (pd.DataFrame({"a": [1, 2, 3], "c": ["x", "y", "z"]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "c", (pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "d", (pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, "d", (pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7.0, 8.0, 9.0]}, "d", (pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7.0, 8.0, 9.0]}), None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "d", (pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}), None)),
])
def test_task_func(data, column, expected_output):
    df, ax = task_func(data, column)
    assert (df.equals(expected_output[0]) and ax == expected_output[1])