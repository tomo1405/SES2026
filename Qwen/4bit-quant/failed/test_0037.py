import pytest
import pandas as pd
import numpy as np
from src_0037 import task_func

def test_task_func_positive_values():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_target_values():
    df = pd.DataFrame({
        'A': [1, 3, 4],
        'B': [1, 3, 4]
    })
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(df)
    plt.close(fig)

def test_task_func_non_target_values():
    df = pd.DataFrame({
        'A': [1, 3, 5],
        'B': [2, 3, 4]
    })
    expected_transformed_df = pd.DataFrame({
        'A': [1, 3, 0],
        'B': [0, 3, 4]
    })
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(expected_transformed_df)
    plt.close(fig)

def test_task_func_constant_column():
    df = pd.DataFrame({
        'A': [3, 3, 3],
        'B': [1, 3, 4]
    })
    expected_transformed_df = pd.DataFrame({
        'A': [3, 3, 3],
        'B': [0, 3, 4]
    })
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(expected_transformed_df)
    plt.close(fig)