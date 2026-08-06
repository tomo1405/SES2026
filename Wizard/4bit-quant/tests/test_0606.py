python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(matrix):
    df = pd.DataFrame(matrix)

    fig, ax = plt.subplots()
    ax.imshow(df, cmap='hot', interpolation='nearest')

    return ax

def test_task_func():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(matrix)
    assert isinstance(ax, plt.Axes)