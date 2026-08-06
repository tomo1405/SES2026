python
import pytest
from src_0231 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'],
                       'Age': [25, 30, 25, 40],
                       'Country': ['USA', 'Canada', 'USA', 'UK'],
                       'Score': [85, 70, 90, 60]})
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

    # Test case 2: Invalid input (not a DataFrame)
    fig = task_func(123)
    assert fig == "Invalid input"

    # Test case 3: Invalid input (duplicate names)
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'],
                       'Age': [25, 30, 25, 40],
                       'Country': ['USA', 'Canada', 'USA', 'UK'],
                       'Score': [85, 70, 90, 60]})
    fig = task_func(df)
    assert fig == "Invalid input"