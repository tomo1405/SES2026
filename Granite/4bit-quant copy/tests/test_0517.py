import pandas as pd
import numpy as np
import statsmodels.api as sm
from src_0517 import task_func
import pytest

def test_task_func():
    array = [["A1", "B1", "C1", "D1", "Response1"], ["A2", "B2", "C2", "D2", "Response2"]]
    df, results = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)
    assert df.shape == (2, 5)
    assert list(df.columns) == ["A", "B", "C", "D", "Response"]
    assert np.array_equal(df["A"], ["A1", "A2"])
    assert np.array_equal(df["B"], ["B1", "B2"])
    assert np.array_equal(df["C"], ["C1", "C2"])
    assert np.array_equal(df["D"], ["D1", "D2"])
    assert np.array_equal(df["Response"], ["Response1", "Response2"])
    X = df[["A", "B", "C", "D"]]
    X = sm.add_constant(X)
    assert np.array_equal(X[:, 0], [1, 1, 0, 0])
    assert np.array_equal(X[:, 1], ["A1", "A2"])
    assert np.array_equal(X[:, 2], ["B1", "B2"])
    assert np.array_equal(X[:, 3], ["C1", "C2"])
    assert np.array_equal(X[:, 4], ["D1", "D2"])
    y = df["Response"]
    assert np.array_equal(y, ["Response1", "Response2"])

def test_task_func_invalid_input():
    array = [["A1", "B1", "C1", "D1"], ["A2", "B2", "C2", "D2", "Response2"]]
    with pytest.raises(ValueError) as e:
        task_func(array)
    assert str(e.value) == "Each sub-list in the input 2D list must have exactly 5 elements."