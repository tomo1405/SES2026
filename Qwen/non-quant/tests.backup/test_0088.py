import pytest
from src_0088 import task_func
import pandas as pd

def test_task_func_basic():
    products = ["A", "B", "C"]
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]
    df = task_func(products, ratings, weights)
    
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Product", "Rating"]
    assert len(df) == len(products)
    assert df["Rating"].max() <= max(ratings)
    assert df["Rating"].min() >= min(ratings)

def test_task_func_reproducibility():
    products = ["A", "B", "C"]
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]
    df1 = task_func(products, ratings, weights)
    df2 = task_func(products, ratings, weights)
    
    assert df1.equals(df2)

def test_task_func_empty_products():
    products = []
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]
    df = task_func(products, ratings, weights)
    
    assert df.empty

def test_task_func_single_product():
    products = ["A"]
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]
    df = task_func(products, ratings, weights)
    
    assert len(df) == 1
    assert df.iloc[0]["Product"] == "A"
    assert df.iloc[0]["Rating"] in ratings

def test_task_func_single_rating():
    products = ["A", "B", "C"]
    ratings = [1]
    weights = [1.0]
    df = task_func(products, ratings, weights)
    
    assert all(df["Rating"] == 1)