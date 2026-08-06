import pandas as pd
from random import choices, seed
from src_0088 import task_func
import pytest

def test_task_func():
    products = ["Product1", "Product2", "Product3"]
    ratings = [1, 2, 3, 4, 5]
    weights = [1, 1, 1, 1, 1]
    random_seed = 42
    df = task_func(products, ratings, weights, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ["Product", "Rating"]
    assert df["Product"].tolist() == products
    assert df["Rating"].tolist() == choices(ratings, weights, k=3)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("Invalid input", [1, 2, 3], [1, 1, 1])