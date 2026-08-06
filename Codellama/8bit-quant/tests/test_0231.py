import pytest
from src_0231 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_valid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                       'Age': [25, 30, 35],
                       'Country': ['USA', 'Canada', 'Mexico'],
                       'Score': [90, 80, 70]})
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)
    assert fig.shape == (10, 5)
    assert len(fig.axes) == 2
    assert fig.axes[0].get_title() == 'Histogram of Scores'
    assert fig.axes[1].get_title() == 'Boxplot of Scores by Country'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                       'Age': [25, 30, 35],
                       'Country': ['USA', 'Canada', 'Mexico'],
                       'Score': [90, 80, 70]})
    fig = task_func(df)
    assert fig == "Invalid input"