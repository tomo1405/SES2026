import pytest
from src_0456 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with valid input
    mean = 0
    std_dev = 1
    n = 1000
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n
    assert np.mean(samples) == pytest.approx(mean, abs=0.1)
    assert np.std(samples) == pytest.approx(std_dev, abs=0.1)

    # Add more assertions to check the plot
    assert plt.gcf().get_axes() is not None
    plt.close()