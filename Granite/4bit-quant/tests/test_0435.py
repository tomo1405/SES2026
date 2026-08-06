import pandas as pd
import re
import random
import pytest

from src_0435 import task_func

def test_task_func():
    s = "1 2 ABC 3.45 This is a test\n2 3 XYZ 4.56 This is another test"
    df = task_func(s)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int

def test_task_func_error():
    with pytest.raises(ValueError):
        task_func("")
    with pytest.raises(ValueError):
        task_func("1 2 3 4 5")