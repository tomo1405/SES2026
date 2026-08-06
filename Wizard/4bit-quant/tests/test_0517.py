python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import pytest

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    COLUMNS = ["A", "B", "C", "D", "Response"]

    np.random.seed(random_seed)

    if not all(len(row) == len(COLUMNS) for row in array):
        raise ValueError(
            "Each sub-list in the input 2D list must have exactly 5 elements."
        )

    df = pd.DataFrame(array, columns=COLUMNS)
    X = df[COLUMNS[:-1]]
    y = df["Response"]
    X = sm.add_constant(X)

    model = sm.OLS(y, X)
    results = model.fit()

    return df, results

def test_task_func():
    # Test case 1: Valid input
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    random_seed = 0
    expected_df = pd.DataFrame(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ],
        columns=["A", "B", "C", "D", "Response"],
    )
    expected_X = expected_df[["A", "B", "C", "D"]]
    expected_y = expected_df["Response"]
    expected_X = sm.add_constant(expected_X)
    expected_model = sm.OLS(expected_y, expected_X)
    expected_results = expected_model.fit()
    expected_output = (expected_df, expected_results)
    actual_output = task_func(array, random_seed)
    assert actual_output == expected_output

    # Test case 2: Invalid input (empty list)
    array = []
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(array, random_seed)

    # Test case 3: Invalid input (list with wrong number of elements)
    array = [
        [1, 2, 3, 4],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(array, random_seed)

    # Test case 4: Invalid input (list with wrong data type)
    array = [
        [1, 2, 3, 4, "5"],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(array, random_seed)