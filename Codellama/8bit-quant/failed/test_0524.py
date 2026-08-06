import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_with_empty_data():
    data = []
    result = task_func(data)
    assert result is None

def test_task_func_with_valid_data():
    data = [1, 2, 3, 4, 5]
    result = task_func(data)
    assert isinstance(result, plt.Axes)
    assert result.get_xlabel() == "Time"
    assert result.get_ylabel() == "Data Points"
    assert result.get_title() == "Data over Time"
    assert len(result.get_lines()) == len(data)
    for i, line in enumerate(result.get_lines()):
        assert line.get_label() == f"Data Point {i}"