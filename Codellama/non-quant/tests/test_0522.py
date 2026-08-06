import pytest
from src_0522 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    assert len(ax.get_lines()) == 3
    for line in ax.get_lines():
        assert isinstance(line, plt.Line2D)
        assert line.get_label() in ["Test 1", "Test 2", "Test 3"]