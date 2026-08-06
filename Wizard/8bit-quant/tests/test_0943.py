python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src_0943 import task_func

def test_task_func():
    sales_df, ax = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(sales_df) == 52
    assert len(sales_df.columns) == 3
    assert len(ax.lines) == 5
    assert ax.get_title() == 'Category-wise Sales Trends'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_ylim() == (0, 400)
    assert ax.get_xlim() == (pd.Timestamp('2016-01-01'), pd.Timestamp('2016-01-13'))
    assert ax.get_xticks().size == 13
    assert ax.get_yticks().size == 5