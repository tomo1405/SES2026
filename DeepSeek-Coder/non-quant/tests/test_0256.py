import pytest
from src_0256 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup():
    fig, ax = plt.subplots()
    yield ax
    plt.close()

def test_task_func(setup):
    ax = setup
    func_index = 0
    with pytest.raises(ValueError):
        task_func(ax, func_index)

def test_task_func_valid(setup):
    ax = setup
    func_index = 0
    task_func(ax, func_index)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "sin(x)"