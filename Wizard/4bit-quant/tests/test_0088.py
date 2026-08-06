python
import pandas as pd
import random
import pytest

from src_0088 import task_func

@pytest.fixture
def products():
    return ["Product A", "Product B", "Product C"]

@pytest.fixture
def ratings():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def weights():
    return [0.1, 0.2, 0.3, 0.2, 0.2]

def test_task_func(products, ratings, weights):
    random.seed(42)
    product_ratings = []

    for product in products:
        rating = random.choices(ratings, weights, k=1)[0]
        product_ratings.append([product, rating])

    df = pd.DataFrame(product_ratings, columns=["Product", "Rating"])
    df.sort_values("Rating", ascending=False, inplace=True)

    assert df.equals(task_func(products, ratings, weights, random_seed=42))