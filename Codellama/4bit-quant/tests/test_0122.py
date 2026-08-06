import matplotlib
import pandas as pd
from src_0122 import task_func


def test_task_func():
    my_list = [1, 2, 3, 4, 5]
    seed = 42
    sales_df, ax = task_func(my_list, seed)

    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert sales_df.shape == (5, 2)
    assert sales_df.columns.tolist() == ['Category', 'Sales']
    assert sales_df['Category'].tolist() == ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    assert sales_df['Sales'].tolist() == [12, 24, 36, 48, 60]
    assert ax.get_title() == 'Category-wise Sales Data'
    assert ax.get_ylabel() == 'Sales'