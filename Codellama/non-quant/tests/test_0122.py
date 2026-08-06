import matplotlib
import pandas as pd
import pytest
from src_0122 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_output_type():
    my_list = [1, 2, 3]
    sales_df, ax = task_func(my_list)
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_output_data():
    my_list = [1, 2, 3]
    sales_df, ax = task_func(my_list)
    assert sales_df.shape == (5, 2)
    assert sales_df['Category'].tolist() == ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    assert sales_df['Sales'].tolist() == [12, 24, 36, 48, 60]
    assert ax.get_title() == 'Category-wise Sales Data'
    assert ax.get_ylabel() == 'Sales'