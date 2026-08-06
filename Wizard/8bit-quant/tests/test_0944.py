python
import pandas as pd
import numpy as np
import pytest
from src_0944 import task_func

def test_task_func():
    # Test with default arguments
    result = task_func()
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert len(result['trend']) == 24
    assert len(result['seasonal']) == 24
    assert len(result['residual']) == 24
    
    # Test with custom arguments
    result = task_func(start_date='2021-01-01', periods=12, freq='W', model='multiplicative')
    assert isinstance(result, dict)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert len(result['trend']) == 12
    assert len(result['seasonal']) == 12
    assert len(result['residual']) == 12
    
    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(start_date='2021-01-01', periods=12, freq='Y', model='invalid')