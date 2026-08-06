import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_0942 import task_func

@pytest.mark.parametrize("start_date, periods, freq, random_seed, expected_shape", [
    ("2023-01-01", 12, "M", 0, (12, 2)),
    ("2023-01-01", 24, "W", 1, (24, 2)),
    ("2023-01-01", 36, "D", 2, (36, 2)),
])
def test_task_func(start_date, periods, freq, random_seed, expected_shape):
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    assert forecast_df.shape == expected_shape
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.grid() is None