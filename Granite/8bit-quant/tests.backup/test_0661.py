import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from src_0661 import task_func
import pytest

def test_task_func():
    x = [np.random.rand(10) for _ in range(3)]
    y = [np.random.rand(10) for _ in range(3)]
    labels = [f"Label {i}" for i in range(3)]

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)  # Check if the returned object is a figure
    assert len(fig.axes) == 1  # Check if the figure has one axis
    assert len(fig.axes[0].lines) == 3  # Check if the axis has three lines (one for each dataset)
    assert fig.axes[0].get_legend().get_texts()[0].get_text() == "Label 0"  # Check if the legend has the correct labels