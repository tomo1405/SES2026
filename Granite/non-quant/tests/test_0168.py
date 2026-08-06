import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from src_0168 import task_func
import pytest

@pytest.fixture
def setup():
    LABELS = [f'Type{i + 1}' for i in range(5)]
    data = pd.DataFrame({label: [randint(0, 100) for _ in range(5)] for label in LABELS})
    return data

def test_task_func_default_args(setup):
    fig, ax = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_args(setup):
    fig, ax = task_func(num_types=3, integer_range=(1, 10))
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)