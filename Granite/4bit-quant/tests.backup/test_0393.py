import pytest
import numpy as np
import matplotlib.pyplot as plt
from src_0393 import task_func

# Constants
COLORS = ['r', 'g', 'b']

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'group_col': ['A', 'B', 'A', 'C', 'B'],
        'value_col': [10, 20, 30, 40, 50]
    })

    # Test with valid input
    ax = task_func(df, 'group_col', 'value_col', 'A')
    assert ax is not None

    # Test with invalid input (group_name not in df)
    with pytest.raises(ValueError):
        task_func(df, 'group_col', 'value_col', 'D')