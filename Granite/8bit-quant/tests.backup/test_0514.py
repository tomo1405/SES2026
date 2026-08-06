import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch
from io import StringIO

from src_0514 import task_func

def test_valid_column():
    column = "Steps"
    data = [
        ["2023-01-01", 100, 200, 5],
        ["2023-01-02", 200, 300, 10],
        ["2023-01-03", 300, 400, 15],
    ]
    expected_result = {
        "sum": 600,
        "mean": 200.0,
        "min": 100,
        "max": 300,
    }
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        result, ax = task_func(column, data)
    assert result == expected_result
    assert ax.get_ylabel() == column
    assert ax.get_title() == f"Line Chart of {column}"

def test_invalid_column():
    column = "Invalid Column"
    data = [
        ["2023-01-01", 100, 200, 5],
        ["2023-01-02", 200, 300, 10],
        ["2023-01-03", 300, 400, 15],
    ]
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        try:
            task_func(column, data)
        except KeyError as e:
            assert str(e) == f"{column} is not a valid column. Choose from {task_func.COLUMNS}."

def test_no_data():
    column = "Steps"
    data = []
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        try:
            task_func(column, data)
        except ValueError as e:
            assert str(e) == "No data to plot."

def test_negative_values():
    column = "Steps"
    data = [
        ["2023-01-01", -100, 200, 5],
        ["2023-01-02", 200, 300, 10],
        ["2023-01-03", 300, 400, 15],
    ]
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        try:
            task_func(column, data)
        except ValueError as e:
            assert str(e) == "Numeric values for steps, calories burned, and distance walked must be non-negative."