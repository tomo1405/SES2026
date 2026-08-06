import pandas as pd
from src_0088 import task_func


def test_task_func():
    products = ["Product 1", "Product 2", "Product 3"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.2, 0.1, 0.4]
    random_seed = 42

    expected_output = pd.DataFrame(
        [
            ["Product 1", 5],
            ["Product 2", 4],
            ["Product 3", 3],
        ],
        columns=["Product", "Rating"],
    )

    output = task_func(products, ratings, weights, random_seed)

    assert output.equals(expected_output)