import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup():
    fig, ax = plt.subplots()
    return ax

def test_task_func(setup):
    ax = setup
    radius = 1
    result = task_func(ax, radius)
    assert result == ax

def test_invalid_radius(setup):
    ax = setup
    radius = -1
    with pytest.raises(ValueError):
        task_func(ax, radius)

def test_invalid_ax_type(setup):
    ax = setup
    radius = 1
    with pytest.raises(TypeError):
        task_func(ax, radius)