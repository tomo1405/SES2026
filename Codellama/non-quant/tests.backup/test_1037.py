import pytest
from src_1037 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([3, 4, 5, 6, 7])
    ax, intersection_len = task_func(s1, s2)

    assert intersection_len == 3
    assert ax.get_title() == f"Overlap Between {s1.name} and {s2.name}"
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_color() == "red"
    assert ax.get_lines()[0].get_linestyle() == "--"