import pandas as pd
from src_0088 import task_func


def test_task_func_returns_dataframe():
    products = ["Product 1", "Product 2", "Product 3"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.2, 0.1, 0.2]
    random_seed = 42

    df = task_func(products, ratings, weights, random_seed)

    assert isinstance(df, pd.DataFrame)


def test_task_func_returns_correct_dataframe():
    products = ["Product 1", "Product 2", "Product 3"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.2, 0.1, 0.2]
    random_seed = 42

    expected_df = pd.DataFrame(
        [
            ["Product 1", 5],
            ["Product 2", 4],
            ["Product 3", 3],
        ],
        columns=["Product", "Rating"],
    )

    df = task_func(products, ratings, weights, random_seed)

    assert df.equals(expected_df)


def test_task_func_returns_correct_dataframe_with_random_seed():
    products = ["Product 1", "Product 2", "Product 3"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.2, 0.1, 0.2]
    random_seed = 1234

    expected_df = pd.DataFrame(
        [
            ["Product 1", 5],
            ["Product 2", 4],
            ["Product 3", 3],
        ],
        columns=["Product", "Rating"],
    )

    df = task_func(products, ratings, weights, random_seed)

    assert df.equals(expected_df)