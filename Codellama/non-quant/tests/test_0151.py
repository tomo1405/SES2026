import matplotlib
import pandas as pd
from src_0151 import task_func


def test_task_func():
    product_dict = {'A': (10, 100), 'B': (20, 200), 'C': (30, 300)}
    product_keys = ['A', 'B', 'C']
    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (3, 5)
    assert df.columns.tolist() == ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    assert df['Product'].tolist() == ['A', 'B', 'C']
    assert df['Quantity'].tolist() == [10, 20, 30]
    assert df['Price'].tolist() == [100, 200, 300]
    assert df['Profit'].tolist() == [1000, 2000, 3000]
    assert df['Average Price'].tolist() == [150, 150, 150]
    assert df['Average Profit'].tolist() == [1500, 1500, 1500]
    assert ax.get_xlabel() == 'Product'
    assert ax.get_ylabel() == 'Profit'
    assert ax.get_title() == 'Profit for each product'