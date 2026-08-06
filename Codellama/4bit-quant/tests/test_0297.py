import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'
    assert len(ax.get_xticks()) == 5
    assert len(ax.get_yticks()) == 5
    assert ax.get_xticks()[0] == 1
    assert ax.get_yticks()[0] == 1
    assert ax.get_xticks()[-1] == 5
    assert ax.get_yticks()[-1] == 5

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(1)