python
import pandas as pd
from random import choices, seed
import pytest

def task_func(products, ratings, weights, random_seed=42):

    seed(random_seed)  # Setting the seed for reproducibility
    product_ratings = []

    for product in products:
        rating = choices(ratings, weights, k=1)[0]
        product_ratings.append([product, rating])

    df = pd.DataFrame(product_ratings, columns=["Product", "Rating"])
    df.sort_values("Rating", ascending=False, inplace=True)

    return df

def test_task_func():
    products = ["Product A", "Product B", "Product C"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    random_seed = 42

    expected_df = pd.DataFrame(
        [["Product C", 5], ["Product B", 4], ["Product A", 3]],
        columns=["Product", "Rating"],
    )

    actual_df = task_func(products, ratings, weights, random_seed)

    assert actual_df.equals(expected_df)