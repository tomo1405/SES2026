import pytest
from src_0231 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                       'Age': [20, 25, 30],
                       'Country': ['USA', 'Canada', 'Mexico'],
                       'Score': [90, 80, 70]})
    result = task_func(df)
    assert isinstance(result, plt.Figure)
    assert result.axes[0].get_title() == 'Histogram of Scores'
    assert result.axes[1].get_title() == 'Boxplot of Scores by Country'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                       'Age': [20, 25, 30],
                       'Country': ['USA', 'Canada', 'Mexico'],
                       'Score': [90, 80, 70]})
    result = task_func(df)
    assert result == "Invalid input"