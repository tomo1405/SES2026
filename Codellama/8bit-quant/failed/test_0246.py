import pytest
from src_0246 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert result['mean'] == 5.0
    assert result['median'] == 5.0
    assert result['mode'] == 5.0

    # Test with custom parameters
    result = task_func(n_data_points=10000, min_value=0.0, max_value=10.0)
    assert result['mean'] == 5.0
    assert result['median'] == 5.0
    assert result['mode'] == 5.0

    # Test with custom parameters and different values
    result = task_func(n_data_points=10000, min_value=1.0, max_value=9.0)
    assert result['mean'] == 5.0
    assert result['median'] == 5.0
    assert result['mode'] == 5.0