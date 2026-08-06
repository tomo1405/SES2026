python
import pandas as pd
import numpy as np
import pytest

def task_func(my_list, seed=42):
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list.")

    if seed is not None:
        np.random.seed(seed)

    my_list.append(12)
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales_data = []
    for category in categories:
        sales = my_list[np.random.randint(0, len(my_list))] * np.random.randint(100, 1000)
        sales_data.append([category, sales])

    sales_df = pd.DataFrame(sales_data, columns=['Category', 'Sales'])

    ax = sales_df.plot(kind='bar', x='Category', y='Sales', legend=False)
    ax.set_title('Category-wise Sales Data')
    ax.set_ylabel('Sales')

    return sales_df, ax

def test_task_func():
    my_list = [10, 20, 30, 40, 50]
    sales_df, ax = task_func(my_list)
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, type(None))
    assert sales_df.shape == (5, 2)
    assert sales_df.columns.tolist() == ['Category', 'Sales']
    assert sales_df['Category'].tolist() == ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    assert sales_df['Sales'].tolist() == [10000, 20000, 30000, 40000, 50000]