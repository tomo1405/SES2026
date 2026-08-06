import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from src_0944 import task_func
import pytest

def test_task_func():
    # Test case 1: Valid input, no error
    result = task_func(start_date='2016-01-01', periods=24, freq='M', model='additive')
    expected_keys = ['trend', 'seasonal', 'residual']
    assert set(result.keys()) == set(expected_keys)
    
    # Test case 2: Invalid input, error should be raised
    with pytest.raises(ValueError):
        task_func(start_date='2016-01-01', periods=24, freq='D', model='additive')