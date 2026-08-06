python
import pandas as pd
import numpy as np
import pytest

from src_0122 import task_func

def test_task_func():
    # Test case 1: Valid input
    my_list = [10, 20, 30, 40, 50]
    sales_df, ax = task_func(my_list)
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)

    # Test case 2: Invalid input (not a list)
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 3: Seed value
    sales_df1, ax1 = task_func(my_list, seed=123)
    sales_df2, ax2 = task_func(my_list, seed=123)
    assert sales_df1.equals(sales_df2)
    assert ax1.equals(ax2)