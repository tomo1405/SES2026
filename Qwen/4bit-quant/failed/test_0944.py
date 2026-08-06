import pytest
from src_0944 import task_func

def test_task_func_default_parameters():
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert result['trend'].shape == (24,)
    assert result['seasonal'].shape == (24,)
    assert result['residual'].shape == (24,)

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
    assert result['trend'].shape == (36,)
    assert result['seasonal'].shape == (36,)
    assert result['residual'].shape == (36,)

def test_task_func_invalid_model():
    result = task_func(model='invalid')
    assert isinstance(result, dict)
    assert 'error' in result
    assert result['error'] == "The model must be either 'additive' or 'multiplicative'."

def test_task_func_invalid_frequency():
    result = task_func(freq='W')
    assert isinstance(result, dict)
    assert 'error' in result
    assert result['error'] == "The frequency must be either 'M' or 'Q'."

def test_task_func_no_trend():
    result = task_func(periods=12)
    assert result['trend'].isnull().all()

def test_task_func_no_seasonal():
    result = task_func(periods=12)
    assert result['seasonal'].isnull().all()

def test_task_func_no_residual():
    result = task_func(periods=12)
    assert result['residual'].isnull().all()