import pytest
from src_0113 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'Status': ['Success', 'Success', 'Failed', 'Success', 'Failed']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Status Distribution'
    assert len(ax.patches) == 2
    assert ax.patches[0].get_height() == 3
    assert ax.patches[1].get_height() == 2
    assert ax.patches[0].get_label() == 'Success'
    assert ax.patches[1].get_label() == 'Failed'