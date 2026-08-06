import pytest
from src_0944 import task_func

def test_task_func_default_parameters():
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert len(result['trend']) == 24
    assert len(result['seasonal']) == 24
    assert len(result['residual']) == 24

def test_task_func_custom_parameters():
    start_date = '2020-01-01'
    periods = 36
    freq = 'Q'
    model = 'multiplicative'
    result = task_func(start_date=start_date, periods=periods, freq=freq, model=model)
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert len(result['trend']) == 36
    assert len(result['seasonal']) == 36
    assert len(result['residual']) == 36

def test_task_func_invalid_model():
    result = task_func(model='invalid')
    assert isinstance(result, dict)
    assert 'error' in result
    assert 'Invalid seasonal component type' in result['error']

def test_task_func_invalid_frequency():
    result = task_func(freq='W')
    assert isinstance(result, dict)
    assert 'error' in result
    assert 'No seasonal decomposition possible' in result['error']