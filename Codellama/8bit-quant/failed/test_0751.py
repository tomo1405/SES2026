import pytest
from src_0751 import task_func
import pandas as pd
import statsmodels.api as sm

def test_task_func_empty_df():
    df = pd.DataFrame()
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert results is None

def test_task_func_no_matching_rows():
    df = pd.DataFrame({'height': [170, 180, 190], 'weight': [50, 60, 70], 'age': [20, 30, 40]})
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert results is None

def test_task_func_valid_input():
    df = pd.DataFrame({'height': [170, 180, 190], 'weight': [50, 60, 70], 'age': [20, 30, 40]})
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)
    assert results.params['const'] == pytest.approx(0.0)
    assert results.params['height'] == pytest.approx(1.0)
    assert results.params['weight'] == pytest.approx(0.0)
    assert results.params['age'] == pytest.approx(0.0)
    assert results.rsquared == pytest.approx(1.0)