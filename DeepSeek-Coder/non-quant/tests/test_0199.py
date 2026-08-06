import pytest
from src_0199 import task_func
import numpy as np
import statistics
import matplotlib.pyplot as plt
import bisect

@pytest.fixture
def setup():
    data = [1, 2, 3, 4, 5]
    value = 3
    return data, value

def test_task_func(setup):
    data, value = setup
    result = task_func(data, value)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], np.ndarray) or isinstance(result[0], list), "The first element should be a numpy array or a list"
    assert isinstance(result[1], int), "The second element should be an integer"
    assert result[1] >= 0, "The second element should be a non-negative integer"

    # Additional assertions can be added to check the specific output values