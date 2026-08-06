import numpy as np
import pandas as pd
import pytest
import statsmodels.api as sm
from src_0517 import task_func


def test_task_func():
    array = [["A1", "B1", "C1", "D1", 1], ["A2", "B2", "C2", "D2", 2]]
    df, results = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)
    assert df.shape == (2, 5)
    assert df.columns.tolist() == ["A", "B", "C", "D", "Response"]
    assert np.array_equal(df["Response"].values, np.array([1, 2]))

def test_task_func_with_seed():
    array = [["A1", "B1", "C1", "D1", 1], ["A2", "B2", "C2", "D2", 2]]
    df1, results1 = task_func(array, random_seed=0)
    df2, results2 = task_func(array, random_seed=0)
    assert np.array_equal(df1, df2)
    assert np.array_equal(results1.params, results2.params)

def test_task_func_with_invalid_input():
    array = [["A1", "B1", "C1", "D1"], ["A2", "B2", "C2", "D2", 2]]
    with pytest.raises(ValueError) as excinfo:
        task_func(array)
    assert "Each sub-list in the input 2D list must have exactly 5 elements." in str(excinfo.value)