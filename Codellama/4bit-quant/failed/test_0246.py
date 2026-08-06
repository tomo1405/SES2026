import pytest
from src_0246 import task_func

def test_task_func():
    # Test with default arguments
    result = task_func()
    assert result['mean'] == pytest.approx(5.0, abs=1e-3)
    assert result['median'] == pytest.approx(5.0, abs=1e-3)
    assert result['mode'] == pytest.approx(5.0, abs=1e-3)

    # Test with custom arguments
    result = task_func(n_data_points=1000, min_value=0.0, max_value=10.0)
    assert result['mean'] == pytest.approx(5.0, abs=1e-3)
    assert result['median'] == pytest.approx(5.0, abs=1e-3)
    assert result['mode'] == pytest.approx(5.0, abs=1e-3)

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(n_data_points=-1000, min_value=0.0, max_value=10.0)
    with pytest.raises(ValueError):
        task_func(n_data_points=1000, min_value=-10.0, max_value=10.0)
    with pytest.raises(ValueError):
        task_func(n_data_points=1000, min_value=0.0, max_value=-10.0)