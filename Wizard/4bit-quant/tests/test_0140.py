python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("The input must be a non-empty pandas DataFrame.")

    numeric_cols = df.select_dtypes(include=np.number).columns
    if not numeric_cols.size:
        raise ValueError("DataFrame contains no numeric columns.")

    axes = []
    for col in numeric_cols:
        fig, ax = plt.subplots()
        df[col].plot(kind='hist', title=col, ax=ax)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)

    return axes

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    axes = task_func(df)
    assert len(axes) == 2
    assert axes[0].get_title() == 'A'
    assert axes[1].get_title() == 'B'

    # Test case 2: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Non-numeric DataFrame
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: DataFrame with no numeric columns
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)