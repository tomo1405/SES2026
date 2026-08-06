import pytest
from src_0507 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def test_task_func_with_valid_input():
    column = "Temperature"
    data = [
        ["2022-01-01", 20, 0.5, 5, 0],
        ["2022-01-02", 22, 0.6, 6, 0],
        ["2022-01-03", 18, 0.7, 7, 0],
    ]
    result = task_func(column, data)

    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 5
    assert result["max"] == 22
    assert isinstance(result["plot"], plt.Axes)


def test_task_func_with_invalid_input():
    column = "Temperature"
    data = [
        ["2022-01-01", 20, 0.5, 5, 0],
        ["2022-01-02", 22, 0.6, 6, 0],
        ["2022-01-03", 18, 0.7, 7, 0],
    ]
    result = task_func(column, data)

    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 5
    assert result["max"] == 22
    assert isinstance(result["plot"], plt.Axes)


def test_task_func_with_empty_data():
    column = "Temperature"
    data = []
    result = task_func(column, data)

    assert result["sum"] == 0
    assert result["mean"] == np.nan
    assert result["min"] == np.inf
    assert result["max"] == -np.inf
    assert isinstance(result["plot"], plt.Axes)