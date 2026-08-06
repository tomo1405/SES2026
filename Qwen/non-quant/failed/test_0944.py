import pytest
from src_0944 import task_func

def test_task_func_default_parameters():
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert isinstance(result['trend'], pd.Series)
    assert isinstance(result['seasonal'], pd.Series)
    assert isinstance(result['residual'], pd.Series)

def test_task_func_custom_parameters():
    start_date = '2020-01-01'
    periods = 36
    freq = 'W'
    model = 'multiplicative'
    result = task_func(start_date=start_date, periods=periods, freq=freq, model=model)
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert isinstance(result['trend'], pd.Series)
    assert isinstance(result['seasonal'], pd.Series)
    assert isinstance(result['residual'], pd.Series)
    assert len(result['trend']) == periods
    assert len(result['seasonal']) == periods
    assert len(result['residual']) == periods

def test_task_func_invalid_model():
    result = task_func(model='invalid')
    assert isinstance(result, dict)
    assert 'error' in result
    assert 'Invalid model type' in result['error']

def test_task_func_invalid_frequency():
    with pytest.raises(ValueError):
        task_func(freq='invalid')

def test_task_func_zero_periods():
    result = task_func(periods=0)
    assert isinstance(result, dict)
    assert 'error' in result
    assert 'Length of values does not match length of index' in result['error']