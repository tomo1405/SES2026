import pytest
from src_0517 import task_func
import pandas as pd
import numpy as np
import statsmodels.api as sm

def test_task_func():
    # Test case 1: Valid input
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, results = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)

    # Test case 2: Invalid input
    array = [[1, 2, 3, 4], [6, 7, 8, 9]]
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 3: Random seed
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df1, results1 = task_func(array, random_seed=0)
    df2, results2 = task_func(array, random_seed=1)
    assert not np.array_equal(df1, df2)
    assert not np.array_equal(results1, results2)