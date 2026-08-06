import pytest
from src_0789 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'col1': np.random.rand(100),
        'col2': np.random.rand(100)
    })

    # Test if the function raises a ValueError when N is less than or equal to 1
    with pytest.raises(ValueError):
        task_func(df, 'col1', 'col2', N=1)

    # Test if the function raises a ValueError when either col1 or col2 is not in the DataFrame
    with pytest.raises(ValueError):
        task_func(df, 'col3', 'col2', N=10)
    with pytest.raises(ValueError):
        task_func(df, 'col1', 'col3', N=10)

    # Test if the function returns a valid p-value
    p_value = task_func(df, 'col1', 'col2', N=10)
    assert 0 <= p_value <= 1