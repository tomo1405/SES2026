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
    df = pd.DataFrame({'Status': ['Open', 'Open', 'Closed', 'Closed']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Status Distribution'
    assert ax.get_xlabel() == 'Status'
    assert ax.get_ylabel() == 'Count'
    assert len(ax.patches) == 2
    assert ax.patches[0]._sizes[0] == 25
    assert ax.patches[1]._sizes[0] == 25
    assert ax.patches[0].get_label() == 'Open'
    assert ax.patches[1].get_label() == 'Closed'

    # Test case 2: Invalid input (not a DataFrame)
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Invalid input (missing 'Status' column)
    df = pd.DataFrame({'Status1': ['Open', 'Open', 'Closed', 'Closed']})
    with pytest.raises(ValueError):
        task_func(df)