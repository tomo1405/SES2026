import pytest
from src_0376 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    return data

def test_task_func(setup):
    result = task_func(setup)
    assert result is not None
    plt.show()