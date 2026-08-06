import pytest
from src_0456 import task_func

def test_task_func():
    # Test with valid inputs
    mean = 0
    std_dev = 1
    n = 100
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n
    assert np.all(samples >= 0)
    assert np.all(samples <= 1)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(mean, std_dev, -1)
    with pytest.raises(ValueError):
        task_func(mean, std_dev, 0)
    with pytest.raises(ValueError):
        task_func(mean, std_dev, 1000001)
    with pytest.raises(ValueError):
        task_func(mean, -1, n)
    with pytest.raises(ValueError):
        task_func(mean, 0, n)
    with pytest.raises(ValueError):
        task_func(mean, 1000001, n)
    with pytest.raises(ValueError):
        task_func(-1, std_dev, n)
    with pytest.raises(ValueError):
        task_func(0, std_dev, n)
    with pytest.raises(ValueError):
        task_func(1000001, std_dev, n)