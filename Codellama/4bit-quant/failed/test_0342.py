import pytest
from src_0342 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: DataFrame is empty
    df = pd.DataFrame()
    col = "a"
    with pytest.raises(ValueError):
        task_func(df, col)

    # Test case 2: Column does not exist
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    col = "c"
    with pytest.raises(ValueError):
        task_func(df, col)

    # Test case 3: Data type is numeric
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    col = "a"
    fig = task_func(df, col)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 2
    assert isinstance(fig.axes[0], plt.Axes)
    assert isinstance(fig.axes[1], plt.Axes)
    assert fig.axes[0].get_title() == "Histogram"
    assert fig.axes[1].get_title() == "Boxplot"

    # Test case 4: Data type is non-numeric
    df = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "e", "f"]})
    col = "a"
    fig = task_func(df, col)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 2
    assert isinstance(fig.axes[0], plt.Axes)
    assert isinstance(fig.axes[1], plt.Axes)
    assert fig.axes[0].get_title() == "Count plot"
    assert fig.axes[1].get_title() == "Strip plot"