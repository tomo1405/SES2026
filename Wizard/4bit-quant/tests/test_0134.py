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
    expected_normalized_df = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    expected_ax = plt.figure().gca()
    expected_ax.plot(expected_normalized_df.index, expected_normalized_df['B'])
    expected_ax.set_title('Normalized Data of B')
    expected_ax.set_xlabel('Index')
    expected_ax.set_ylabel('Normalized Value')
    expected_ax.set_ylim(0, 1)
    expected_ax.set_xlim(0, 2)

    actual_normalized_df, actual_ax = task_func(df)

    assert actual_normalized_df.equals(expected_normalized_df)
    assert actual_ax.get_title() == expected_ax.get_title()
    assert actual_ax.get_xlabel() == expected_ax.get_xlabel()
    assert actual_ax.get_ylabel() == expected_ax.get_ylabel()
    assert actual_ax.get_ylim() == expected_ax.get_ylim()
    assert actual_ax.get_xlim() == expected_ax.get_xlim()

    # Test case 2: Empty input
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Non-DataFrame input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test case 4: Non-numeric column input
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df)