import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_input_not_dataframe():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_dataframe():
    df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'
    assert len(ax.get_xticks()) == 5
    assert len(ax.get_yticks()) == 5
    assert ax.get_xticks()[0] == 1
    assert ax.get_xticks()[1] == 2
    assert ax.get_xticks()[2] == 3
    assert ax.get_xticks()[3] == 4
    assert ax.get_xticks()[4] == 5
    assert ax.get_yticks()[0] == 1
    assert ax.get_yticks()[1] == 2
    assert ax.get_yticks()[2] == 3
    assert ax.get_yticks()[3] == 4
    assert ax.get_yticks()[4] == 5