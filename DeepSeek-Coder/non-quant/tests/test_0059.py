import pytest
from src_0059 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

@pytest.fixture
def setup():
    mu = 0
    sigma = 1
    num_samples = 1000
    return mu, sigma, num_samples

def test_task_func(setup):
    mu, sigma, num_samples = setup
    fig = task_func(mu, sigma, num_samples)
    assert fig is not None
    plt.close()