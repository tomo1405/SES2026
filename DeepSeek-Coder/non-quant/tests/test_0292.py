import pytest
from src_0292 import task_func
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

@pytest.fixture(scope="module")
def setup():
    plt.figure()
    yield
    plt.close()

def test_task_func(setup):
    mu, sigma = 0, 1
    result = task_func(mu, sigma)
    assert result is not None
    assert plt.gcf().get_axes()