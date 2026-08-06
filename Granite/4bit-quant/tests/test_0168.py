import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from src_0168 import task_func
import pytest

def test_task_func():
    num_types = 5
    integer_range = (0, 100)
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = task_func(num_types, integer_range)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Type'
    assert ax.get_title() == 'Bar Plot of Random Data'