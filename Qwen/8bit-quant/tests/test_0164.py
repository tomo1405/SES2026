import pytest
from src_0164 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    data = pd.DataFrame(np.random.rand(5, 5) * 100, columns=['A', 'B', 'C', 'D', 'E'])
    assert ax.get_legend().get_texts()[0].get_text() == 'A'

def test_task_func_custom_size():
    ax = task_func(rows=3, cols=3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    data = pd.DataFrame(np.random.rand(3, 3) * 100, columns=['A', 'B', 'C'])
    assert ax.get_legend().get_texts()[0].get_text() == 'A'

def test_task_func_max_columns():
    ax = task_func(cols=5)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    data = pd.DataFrame(np.random.rand(5, 5) * 100, columns=['A', 'B', 'C', 'D', 'E'])
    assert ax.get_legend().get_texts()[0].get_text() == 'A'

def test_task_func_value_error():
    with pytest.raises(ValueError, match="Maximum number of columns allowed is 5"):
        task_func(cols=6)