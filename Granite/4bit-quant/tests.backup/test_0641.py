import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from src_0641 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame"
    assert df.shape == (12, 5), "The DataFrame should have 12 rows and 5 columns"
    assert df.index.tolist() == ['Month1', 'Month2', 'Month3', 'Month4', 'Month5', 'Month6', 'Month7', 'Month8', 'Month9', 'Month10', 'Month11', 'Month12'], "The index of the DataFrame should be the months"
    assert df.columns.tolist() == ['Product1', 'Product2', 'Product3', 'Product4', 'Product5'], "The columns of the DataFrame should be the products"
    assert df.loc['Month1', 'Product1'] > 0 and df.loc['Month1', 'Product1'] < 1001, "The sales value for Product1 in Month1 should be between 100 and 1000"
    assert df.loc['Month12', 'Product5'] > 0 and df.loc['Month12', 'Product5'] < 1001, "The sales value for Product5 in Month12 should be between 100 and 1000"
    assert plt.fignum_exists(1) and plt.fignum_exists(2), "The function should create two figures using matplotlib"
    assert len(plt.figure(1).axes) == 1 and len(plt.figure(2).axes) == 1, "The figures should have one axis each"
    assert plt.figure(1).axes[0].get_ylabel() == 'Total Sales', "The y-label of the first figure should be 'Total Sales'"
    assert plt.figure(2).axes[0].get_title() == 'Monthly Sales per Product', "The title of the second figure should be 'Monthly Sales per Product'"