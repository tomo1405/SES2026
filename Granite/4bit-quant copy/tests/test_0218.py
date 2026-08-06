import pytest
from src_0218 import task_func

def test_task_func():
    ax, mean, std = task_func()
    assert ax is not None, "Expected ax to be a valid object, but it's None"
    assert mean is not None, "Expected mean to be a valid value, but it's None"
    assert std is not None, "Expected std to be a valid value, but it's None"
    assert isinstance(mean, float), "Expected mean to be a float, but it's not"
    assert isinstance(std, float), "Expected std to be a float, but it's not"
    assert mean == pytest.approx(0, abs=0.1), "Expected mean to be close to 0, but it's not"
    assert std == pytest.approx(1, abs=0.1), "Expected std to be close to 1, but it's not"