import matplotlib.pyplot as plt
import pandas as pd
from src_0151 import task_func


def test_task_func():
    product_dict = {'A': (10, 100), 'B': (20, 200), 'C': (30, 300)}
    product_keys = ['A', 'B', 'C']
    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.columns.tolist() == ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    assert df['Average Price'].tolist() == [150, 250, 350]
    assert df['Average Profit'].tolist() == [1500, 2500, 3500]
    assert ax.get_title() == "Profit for each product"
    assert ax.get_ylabel() == "Profit"