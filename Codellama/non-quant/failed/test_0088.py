import pytest
from src_0088 import task_func


def test_task_func():
    products = ["A", "B", "C"]
    ratings = [1, 2, 3]
    weights = [0.2, 0.3, 0.5]
    random_seed = 42

    expected_output = pd.DataFrame(
        [
            ["A", 3],
            ["B", 2],
            ["C", 1],
        ],
        columns=["Product", "Rating"],
    )

    output = task_func(products, ratings, weights, random_seed)

    assert output.equals(expected_output)