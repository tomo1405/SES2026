import pytest
from src_0981 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def test_task_func_no_numeric_columns():
    df = pd.DataFrame({'a': ['x', 'y'], 'b': ['z', 'w']})
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == "No numeric columns present"

def test_task_func_with_numeric_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['x', 'y', 'z']
    })
    transformed_df, fig = task_func(df)

    # Check if the DataFrame is scaled correctly
    scaler = StandardScaler()
    expected_scaled_data = scaler.fit_transform(df[['A', 'B']])
    assert np.allclose(transformed_df[['A', 'B']].values, expected_scaled_data)

    # Check if the figure is created
    assert isinstance(fig, plt.Figure)

def test_task_func_all_numeric_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    transformed_df, fig = task_func(df)

    # Check if the DataFrame is scaled correctly
    scaler = StandardScaler()
    expected_scaled_data = scaler.fit_transform(df[['A', 'B']])
    assert np.allclose(transformed_df[['A', 'B']].values, expected_scaled_data)

    # Check if the figure is created
    assert isinstance(fig, plt.Figure)