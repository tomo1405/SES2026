import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from unittest.mock import patch

from src_0231 import task_func

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def test_task_func_invalid_input():
    invalid_input = "Invalid input"
    assert task_func("invalid input") == invalid_input
    assert task_func(123) == invalid_input
    assert task_func(None) == invalid_input

@patch("matplotlib.pyplot.show")
def test_task_func_valid_input(mock_show):
    valid_input = pd.DataFrame(columns=COLUMNS)
    fig = task_func(valid_input)
    assert isinstance(fig, plt.Figure)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_task_func_valid_input_with_duplicates(mock_show):
    df = pd.DataFrame(columns=COLUMNS)
    df = df.append([df] * 2, ignore_index=True)
    df = df.drop_duplicates(subset='Name', keep=False)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)
    mock_show.assert_called_once()