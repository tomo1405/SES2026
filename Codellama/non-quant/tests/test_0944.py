import pytest
from src_0944 import task_func

def test_task_func():
    # Test with valid input
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(start_date='2016-01-01', periods=24, freq='M', model='invalid')