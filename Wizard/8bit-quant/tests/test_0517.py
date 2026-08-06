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
    input_array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    expected_df = pd.DataFrame(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ],
        columns=["A", "B", "C", "D", "Response"],
    )
    expected_results = sm.OLS(
        expected_df["Response"],
        sm.add_constant(expected_df[["A", "B", "C", "D"]]),
    ).fit()
    actual_df, actual_results = task_func(input_array)
    assert expected_df.equals(actual_df)
    assert expected_results.summary().as_text() == actual_results.summary().as_text()

    # Test case 2: Invalid input (not all rows have 5 elements)
    input_array = [
        [1, 2, 3, 4],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    with pytest.raises(ValueError):
        task_func(input_array)

    # Test case 3: Invalid input (not all elements are numeric)
    input_array = [
        [1, 2, 3, "4", 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    with pytest.raises(ValueError):
        task_func(input_array)

    # Test case 4: Invalid input (not all elements are finite)
    input_array = [
        [1, 2, 3, float("nan"), 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    with pytest.raises(ValueError):
        task_func(input_array)