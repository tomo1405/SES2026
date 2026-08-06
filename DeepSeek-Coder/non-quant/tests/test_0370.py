import pytest
from src_0370 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

@pytest.fixture
def sample_data():
    return np.random.normal(0, 1, 100)

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert result is not None
    assert plt.gcf().get_axes() is not None
    plt.close()