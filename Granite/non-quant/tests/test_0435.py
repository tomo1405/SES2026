import pandas as pd
import re
import random
import pytest
from src_0435 import task_func

def test_task_func():
    s = "1 2 ABC 3.0 description\n4 5 XYZ 4.0 description"
    df = task_func(s)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int

def test_task_func_with_seed():
    s = "1 2 ABC 3.0 description\n4 5 XYZ 4.0 description"
    df1 = task_func(s, seed=0)
    df2 = task_func(s, seed=0)
    assert df1.equals(df2)

def test_task_func_with_invalid_data():
    s = "1 2 ABC 3.0 description\n4 5 XYZ 4.0 description\n6 7"
    with pytest.raises(ValueError):
        task_func(s)