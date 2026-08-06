import pytest
from src_0920 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
    column = 'A'
    ax = task_func(data, column)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Category'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == f'Distribution of {column}'
    assert len(ax.get_xticklabels()) == 5
    assert len(ax.get_yticklabels()) == 5
    assert ax.get_xticklabels()[0].get_text() == 'A'
    assert ax.get_yticklabels()[0].get_text() == '1'
    assert ax.get_xticklabels()[4].get_text() == 'E'
    assert ax.get_yticklabels()[4].get_text() == '5'