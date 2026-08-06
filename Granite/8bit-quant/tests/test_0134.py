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
    # Test case 1: Input is not a DataFrame
    with pytest.raises(ValueError) as exc_info:
        task_func("not a DataFrame")
    assert "Input must be a non-empty DataFrame." in str(exc_info.value)

    # Test case 2: Input DataFrame is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(df)
    assert "Input must be a non-empty DataFrame." in str(exc_info.value)

    # Test case 3: Normal input
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6],
        "col3": [7, 8, 9]
    })
    normalized_df, ax = task_func(df)
    assert isinstance(normalized_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(normalized_df.columns) == 1
    assert normalized_df.columns[0] == df.columns[-1]
    assert (normalized_df[df.columns[-1]] != df[df.columns[-1]]).any()