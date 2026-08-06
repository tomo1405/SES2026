import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import pytest

def task_func(num_rows=5, rand_range=(0, 100)):
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

def test_task_func():
    # Test case 1: Default arguments
    fig = task_func()
    assert isinstance(fig, plt.Figure)

    # Test case 2: Custom arguments
    fig = task_func(num_rows=10, rand_range=(1, 10))
    assert isinstance(fig, plt.Figure)