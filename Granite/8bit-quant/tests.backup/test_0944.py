import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from src_0944 import task_func

def test_task_func_with_default_args():
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result and 'seasonal' in result and 'residual' in result

def test_task_func_with_custom_args():
    start_date = '2022-01-01'
    periods = 12
    freq = 'M'
    model = 'multiplicative'
    result = task_func(start_date, periods, freq, model)
    assert isinstance(result, dict)
    assert 'trend' in result and 'seasonal' in result and 'residual' in result

def test_task_func_with_invalid_args():
    start_date = '2022-01-01'
    periods = 12
    freq = 'M'
    model = 'invalid_model'
    result = task_func(start_date, periods, freq, model)
    assert isinstance(result, dict)
    assert 'error' in result