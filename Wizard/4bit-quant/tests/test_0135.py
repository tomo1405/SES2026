python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df, bins=20):

    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("The input must be a non-empty pandas DataFrame.")

    last_col_name = df.columns[-1]
    fig, ax = plt.subplots()
    ax.hist(df[last_col_name], bins=bins)
    ax.set_title(f'Histogram of {last_col_name}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.show()
    return ax

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Invalid input (empty DataFrame)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Invalid input (non-DataFrame input)
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test case 4: Invalid input (non-numeric column)
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'], 'B': [2, 4, 6, 8, 10]})
    with pytest.raises(ValueError):
        task_func(df)