import pytest
from src_0944 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result = task_func()
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result

    # Test case 2: Custom start date, periods, and frequency
    result = task_func(start_date='2023-01-01', periods=12, freq='M')
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result

    # Test case 3: Invalid model parameter
    result = task_func(model='invalid_model')
    assert 'error' in result

    # Test case 4: Monthly frequency
    result = task_func(freq='M')
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result

    # Test case 5: Quarterly frequency
    result = task_func(freq='Q')
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result