import pytest
from src_0517 import task_func
import pandas as pd
import numpy as np
import statsmodels.api as sm

def test_task_func():
    # Test case 1: Basic functionality
    array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    result = task_func(array)
    assert isinstance(result, tuple)
    assert isinstance(result[0], pd.DataFrame)
    assert isinstance(result[1], sm.regression.linear_model.RegressionResultsWrapper)

    # Test case 2: Invalid input
    array = [
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1]
    ]
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 3: Check random seed
    np.random.seed(0)
    array = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    result1 = task_func(array)
    np.random.seed(0)
    result2 = task_func(array)
    assert result1 == result2