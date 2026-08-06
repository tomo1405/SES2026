python
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import pytest

def task_func(num_types=5, integer_range=(0, 100)):
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = plt.subplots()
    data.plot(kind='barh', stacked=True, ax=ax)

    return fig, ax

def test_task_func():
    fig, ax = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Type'
    assert ax.get_title() == 'Task Function'