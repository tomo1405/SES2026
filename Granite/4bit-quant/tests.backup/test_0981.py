import pytest
from src_0981 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Create a sample dataframe with numeric and non-numeric columns
    df = pd.DataFrame({
        'numeric_col1': np.random.rand(10),
        'numeric_col2': np.random.rand(10),
        'non_numeric_col': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    })

    # Call the function and store the returned values
    df_transformed, fig = task_func(df)

    # Assert that the returned values are of the expected type
    assert isinstance(df_transformed, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Assert that the function raises a ValueError when the dataframe has no numeric columns
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'col1': ['a', 'b', 'c', 'd', 'e']}))