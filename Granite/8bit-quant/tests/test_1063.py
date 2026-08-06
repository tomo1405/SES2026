import pandas as pd
import pytest
from matplotlib import pyplot as plt
from src_1063 import task_func

@pytest.mark.parametrize("arr, expected_title", [
    (pd.Series([1, 2, 3]), "Time Series of Row Sums"),
    (pd.Series([]), "Time Series of Row Sums"),
    (pd.DataFrame([[1, 2], [3, 4]]), "Time Series of Row Sums"),
])
def test_task_func(arr, expected_title):
    ax = task_func(arr)
    assert ax.get_title() == expected_title