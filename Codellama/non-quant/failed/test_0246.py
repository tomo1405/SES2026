import pytest
from src_0246 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert result['mean'] == pytest.approx(5.0, abs=0.1)
    assert result['median'] == pytest.approx(5.0, abs=0.1)
    assert result['mode'] == pytest.approx(5.0, abs=0.1)

    # Test with custom parameters
    result = task_func(n_data_points=10000, min_value=0.0, max_value=10.0)
    assert result['mean'] == pytest.approx(5.0, abs=0.1)
    assert result['median'] == pytest.approx(5.0, abs=0.1)
    assert result['mode'] == pytest.approx(5.0, abs=0.1)

    # Test with custom parameters
    result = task_func(n_data_points=10000, min_value=0.0, max_value=10.0)
    assert result['mean'] == pytest.approx(5.0, abs=0.1)
    assert result['median'] == pytest.approx(5.0, abs=0.1)
    assert result['mode'] == pytest.approx(5.0, abs=0.1)

    # Test with custom parameters
    result = task_func(n_data_points=10000, min_value=0.0, max_value=10.0)
    assert result['mean'] == pytest.approx(5.0, abs=0.1)
    assert result['median'] == pytest.approx(5.0, abs=0.1)
    assert result['mode'] == pytest.approx(5.0, abs=0.1)