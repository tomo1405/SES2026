python
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import pytest

def task_func(directory: str, pattern: str) -> list:

    plots = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            df = pd.read_csv(os.path.join(directory, file))
            ax = df.plot(x='Month', y='Sales', title=file)
            plots.append(ax)
    plt.show()
    return plots

def test_task_func():
    directory = 'data'
    pattern = r'^\d{4}-\d{2}-\d{2}.csv$'
    plots = task_func(directory, pattern)
    assert len(plots) == 2
    assert isinstance(plots[0], plt.Axes)
    assert isinstance(plots[1], plt.Axes)