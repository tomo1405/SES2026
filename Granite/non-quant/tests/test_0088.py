import pandas as pd
from random import choices, seed
from src_0088 import task_func
import pytest

@pytest.fixture
def products():
    return ["Product1", "Product2", "Product3"]

@pytest.fixture
def ratings():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def weights():
    return [0.2, 0.2, 0.2, 0.2, 0.2]

def test_task_func(products, ratings, weights):
    df = task_func(products, ratings, weights)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(products), 2)
    assert df.columns.tolist() == ["Product", "Rating"]
    assert df["Product"].tolist() == products
    assert all(df["Rating"].between(1, 5))

def test_task_func_with_seed(products, ratings, weights):
    df1 = task_func(products, ratings, weights, random_seed=42)
    df2 = task_func(products, ratings, weights, random_seed=42)
    assert df1.equals(df2)

def test_task_func_with_invalid_seed(products, ratings, weights):
    df1 = task_func(products, ratings, weights, random_seed=42)
    df2 = task_func(products, ratings, weights, random_seed=123)
    assert not df1.equals(df2)