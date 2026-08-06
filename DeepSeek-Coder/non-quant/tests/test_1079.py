import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    np.random.seed(0)
    arr = np.random.randint(0, 10, size=10)
    return arr

def test_task_func(setup):
    arr = setup
    result, _ = task_func(arr)
    assert result is not None

def test_uniform_distribution(setup):
    arr = setup
    _, ax = task_func(arr)
    assert ax is not None

def test_plot_creation(setup):
    arr = setup
    _, ax = task_func(arr)
    assert ax is not None