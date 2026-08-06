import pytest
from src_1002 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv():
    data = u"""column1
1
2
3
4
5"""
    return io.StringIO(data)

def test_task_func(sample_csv):
    ax = task_func(sample_csv)
    
    # Check if the axes object is returned
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct number of lines
    lines = ax.get_lines()
    assert len(lines) == 1
    
    # Check if the plot has the correct title
    assert ax.get_title() == "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    
    # Check if the plot has the correct x label
    assert ax.get_xlabel() == "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    
    # Check if the plot has the correct y label
    assert ax.get_ylabel() == "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    
    # Check if the normalization is done correctly
    df = pd.read_csv(sample_csv)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std
    expected_ydata = df["column1_normalized"].values
    assert all(lines[0].get_ydata() == expected_ydata)