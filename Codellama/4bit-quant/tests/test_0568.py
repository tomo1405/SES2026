import pytest
from src_0568 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    data = '1-2-3-4-5-6-7-8-9-10'
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Values'
    assert ax.get_xticks() == sorted(list(set(data.split('-'))))
    assert ax.get_yticks() == np.arange(1, 11)
    assert ax.get_xlim() == (1, 10)
    assert ax.get_ylim() == (0, 10)