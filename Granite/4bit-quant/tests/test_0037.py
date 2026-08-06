import numpy as np
import pandas as pd
import pytest
from src_0037 import task_func

TARGET_VALUES = np.array([1, 3, 4])

def test_task_func():
    # Test if the function raises a ValueError when the DataFrame contains negative values
    df_neg = pd.DataFrame({
        'A': [-1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(df_neg)

    # Test if the function raises a ValueError when the DataFrame contains non-numeric values
    df_non_numeric = pd.DataFrame({
        'A': ['a', 'b', 'c'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(df_non_numeric)

    # Test if the function returns the expected output for a DataFrame with constant values
    df_constant = pd.DataFrame({
        'A': [1, 1, 1],
        'B': [3, 3, 3]
    })
    expected_output = pd.DataFrame({
        'A': [1, 1, 1],
        'B': [3, 3, 3]
    })
    output_df, _ = task_func(df_constant)
    assert output_df.equals(expected_output)

    # Test if the function returns the expected output for a DataFrame with non-constant values
    df_non_constant = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    expected_output = pd.DataFrame({
        'A': [0.34826269, 1.26276972, 3.00000000],
        'B': [4.00000000, 5.00000000, 6.00000000]
    })
    output_df, _ = task_func(df_non_constant)
    assert output_df.equals(expected_output)

if __name__ == "__main__":
    pytest.main()