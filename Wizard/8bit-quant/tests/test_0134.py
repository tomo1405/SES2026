python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    last_col_name = df.columns[-1]
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(df[[last_col_name]])
    normalized_df = df.copy()
    normalized_df[last_col_name] = normalized_values.flatten()
    
    fig, ax = plt.subplots()
    ax.plot(normalized_df.index, normalized_df[last_col_name])
    ax.set_title(f'Normalized Data of {last_col_name}')
    ax.set_xlabel("Index")
    ax.set_ylabel("Normalized Value")

    return normalized_df, ax

def test_task_func():
    # Test case 1: Normal input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_df = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    expected_ax = None
    result_df, result_ax = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_ax == result_ax
    
    # Test case 2: Empty input
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())
    
    # Test case 3: Non-DataFrame input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])