import pytest
from src_0260 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup():
    fig, ax = plt.subplots()
    return ax

def test_task_func(setup):
    ax = setup
    num_points = 10
    result = task_func(ax, num_points)
    assert result == ax

def test_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid_input", 10)