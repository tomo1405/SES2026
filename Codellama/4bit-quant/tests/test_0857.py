import pytest
from src_0857 import task_func

def test_task_func():
    # Test with default parameters
    result, matrix = task_func()
    assert result == 120
    assert matrix.shape == (3, 3)
    assert np.all(matrix >= 1) and np.all(matrix <= 10)

    # Test with custom parameters
    result, matrix = task_func(shape=(4, 4), low=0, high=100)
    assert result == 120
    assert matrix.shape == (4, 4)
    assert np.all(matrix >= 0) and np.all(matrix <= 100)

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(shape=(3, 3), low=10, high=1)