import pytest
from src_0808 import task_func
import numpy as np
from scipy.stats import norm

@pytest.fixture
def data():
    return np.array([1, 2, 3, 4, 5, 100])

def test_task_func(data):
    result = task_func(data)
    assert isinstance(result, list)
    assert len(result) == 3
    assert isinstance(result[0], list)
    assert isinstance(result[1], float)
    assert isinstance(result[2], float)

def test_zero_std_dev(data):
    data = np.array([1, 2, 3, 4, 5])
    result = task_func(data)
    assert result == ([], 3.0, 2.0)