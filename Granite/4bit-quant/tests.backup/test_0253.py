import matplotlib.pyplot as plt
from itertools import zip_longest
# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    fig, ax = plt.subplots()
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
        
    ax.legend()
    return ax
import pytest

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = ['Series 1', 'Series 2', 'Series 3']
    ax = task_func(data, labels)
    assert ax.legend_.texts[0].get_text() == 'Series 1'
    assert ax.legend_.texts[1].get_text() == 'Series 2'
    assert ax.legend_.texts[2].get_text() == 'Series 3'