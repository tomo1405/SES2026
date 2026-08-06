import pandas as pd
import pytest
from src_0435 import task_func

def test_task_func():
    s = """1 10 APPLE 100 Apple
2 20 BANANA 200 Banana
3 30 ORANGE 300 Orange
4 40 PEAR 400 Pear
5 50 GRAPE 500 Grape"""
    df = task_func(s)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["ID"].tolist() == [1, 2, 3, 4, 5]
    assert df["Quantity"].tolist() == [10, 20, 30, 40, 50]
    assert df["Code"].tolist() == ["APPLE", "BANANA", "ORANGE", "PEAR", "GRAPE"]
    assert df["Price"].tolist() == [100, 200, 300, 400, 500]
    assert df["Product"].tolist() != ["APPLE", "BANANA", "ORANGE", "PEAR", "GRAPE"]
    assert df["Description"].tolist() == ["Apple", "Banana", "Orange", "Pear", "Grape"]

def test_task_func_with_seed():
    s = """1 10 APPLE 100 Apple
2 20 BANANA 200 Banana
3 30 ORANGE 300 Orange
4 40 PEAR 400 Pear
5 50 GRAPE 500 Grape"""
    df1 = task_func(s, seed=0)
    df2 = task_func(s, seed=0)
    assert df1.equals(df2)

def test_task_func_with_invalid_data():
    s = """1 10 APPLE 100 Apple
2 20 BANANA 200 Banana
3 30 ORANGE 300 Orange
4 40 PEAR 400 Pear
5 50 GRAPE 500 Grape
6 60 watermelon 600 Watermelon"""
    with pytest.raises(ValueError) as excinfo:
        task_func(s)
    assert "Incomplete data provided." in str(excinfo.value)