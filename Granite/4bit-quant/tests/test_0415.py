import pandas as pd
import numpy as np
import pytest

from src_0415 import task_func

@pytest.mark.parametrize("data, column, expected", [
    ({"a": [1, 2, 3], "b": [4, 5, 6]}, "a", ({"b": [4, 5, 6]}, None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, "b", ({"a": [1, 2, 3], "c": [7, 8, 9]}, None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7.0, 8.0, 9.0]}, "b", ({"a": [1, 2, 3], "c": [7.0, 8.0, 9.0]}, None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "b", ({"a": [1, 2, 3], "c": ["x", "y", "z"]}, None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "a", ({"b": [4, 5, 6], "c": ["x", "y", "z"]}, None)),
    ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, "d", ({"a": [1, 2, 3], "b": [4, 5, 6], "c": ["x", "y", "z"]}, None)),
])
def test_task_func(data, column, expected):
    df, ax = task_func(data, column)
    assert (df, ax) == expected