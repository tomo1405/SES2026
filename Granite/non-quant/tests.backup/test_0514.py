import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src_0514 import task_func

def test_valid_column():
    column = "Steps"
    data = [
        ["2022-01-01", 100, 200, 5],
        ["2022-01-02", 200, 300, 10],
        ["2022-01-03", 300, 400, 15],
    ]
    expected_result = {
        "sum": 600,
        "mean": 200.0,
        "min": 100,
        "max": 300,
    }
    expected_ax = None  # We don't test the plot here

    result, ax = task_func(column, data)

    assert result == expected_result
    assert ax == expected_ax

def test_invalid_column():
    column = "Invalid Column"
    data = [
        ["2022-01-01", 100, 200, 5],
        ["2022-01-02", 200, 300, 10],
        ["2022-01-03", 300, 400, 15],
    ]

    with pytest.raises(KeyError) as exc_info:
        task_func(column, data)

    assert str(exc_info.value) == f"{column} is not a valid column. Choose from {COLUMNS}."

def test_no_data():
    column = "Steps"
    data = []

    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)

    assert str(exc_info.value) == "No data to plot."

def test_negative_values():
    column = "Steps"
    data = [
        ["2022-01-01", -100, 200, 5],
        ["2022-01-02", 200, 300, 10],
        ["2022-01-03", 300, -400, 15],
    ]

    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)

    assert str(exc_info.value) == "Numeric values for steps, calories burned, and distance walked must be non-negative."