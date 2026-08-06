python
import pandas as pd
import random
import pytest

from src_0088 import task_func

def test_task_func():
    products = ["Product A", "Product B", "Product C"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    random_seed = 42

    expected_df = pd.DataFrame(
        [
            ["Product C", 5],
            ["Product A", 4],
            ["Product B", 3],
        ],
        columns=["Product", "Rating"],
    )

    actual_df = task_func(products, ratings, weights, random_seed)

    assert actual_df.equals(expected_df)