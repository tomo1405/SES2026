import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = [1, 2, 3, 4, 5]
    result = task_func(data)
    assert result is not None
    assert isinstance(result, plt.gca)
    assert result.xlabel == "Time"
    assert result.ylabel == "Data Points"
    assert result.title == "Data over Time"
    assert len(result.lines) == len(data)
    for i, line in enumerate(result.lines):
        assert line.get_label() == f"Data Point {i}"