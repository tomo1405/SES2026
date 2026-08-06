import pytest
from src_0313 import task_func
import random
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    random.seed(42)
    plt.switch_backend('agg')

def test_task_func_default_args(setup):
    distribution, ax = task_func()
    assert len(distribution) == 1000
    assert len(ax) == 30

def test_task_func_custom_args(setup):
    distribution, ax = task_func(bins=50)
    assert len(distribution) == 1000
    assert len(ax) == 50