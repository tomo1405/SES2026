import pytest
from src_0522 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data_list = [
        {"name": "Alice", "score": 100},
        {"name": "Bob", "score": 90},
        {"name": "Charlie", "score": 80},
    ]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_label() == "Alice"
    assert ax.get_lines()[1].get_label() == "Bob"
    assert ax.get_lines()[2].get_label() == "Charlie"