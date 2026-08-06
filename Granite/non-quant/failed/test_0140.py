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
    # Test case 1: input is not a pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(np.array([[1, 2, 3], [4, 5, 6]]))
    assert "The input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 2: input is an empty pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame())
    assert "The input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 3: input is a pandas DataFrame with no numeric columns
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "DataFrame contains no numeric columns." in str(excinfo.value)

    # Test case 4: input is a pandas DataFrame with numeric columns
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4.0, 5.0, 6.0]})
    axes = task_func(df)
    assert len(axes) == 2
    assert isinstance(axes[0], plt.Axes)
    assert isinstance(axes[1], plt.Axes)