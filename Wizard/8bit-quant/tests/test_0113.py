python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or 'Status' not in df.columns:
        raise ValueError("Input must be a pandas DataFrame with a 'Status' column.")

    status_counts = df['Status'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
    ax.set_title('Status Distribution')

    return ax

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'Status': ['Open', 'Open', 'Closed']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Invalid input (not a DataFrame)
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Invalid input (no 'Status' column)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'Name': ['John', 'Jane', 'Bob']}))