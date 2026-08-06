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
    # Test case 1: Input is not a pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func([['Yes', 'No'], ['Yes', 'No']])
    assert "Input must be a pandas DataFrame with a 'Status' column." in str(excinfo.value)

    # Test case 2: Input is a pandas DataFrame but does not have a 'Status' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "Input must be a pandas DataFrame with a 'Status' column." in str(excinfo.value)

    # Test case 3: Input is a valid pandas DataFrame
    df = pd.DataFrame({'Status': ['Yes', 'No', 'Yes', 'Yes', 'No']})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)