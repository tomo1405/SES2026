import pandas as pd
from src_0641 import task_func


def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame"
    assert df.shape == (12, 5), "The DataFrame should have 12 rows and 5 columns"
    assert df.index.tolist() == MONTHS, "The index of the DataFrame should be the list of months"
    assert df.columns.tolist() == PRODUCTS, "The columns of the DataFrame should be the list of products"