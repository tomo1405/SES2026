import pytest
from src_0113 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    df = pd.DataFrame({'Status': ['A', 'B', 'C', 'A', 'B', 'C']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Status Distribution'
    assert len(ax.get_legend().get_texts()) == 3
    assert ax.get_legend().get_texts()[0].get_text() == 'A'
    assert ax.get_legend().get_texts()[1].get_text() == 'B'
    assert ax.get_legend().get_texts()[2].get_text() == 'C'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Status': ['A', 'B', 'C', 'A', 'B', 'C']})
    with pytest.raises(ValueError):
        task_func(df)