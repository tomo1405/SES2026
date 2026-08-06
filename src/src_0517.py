import pandas as pd
import numpy as np
import statsmodels.api as sm
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