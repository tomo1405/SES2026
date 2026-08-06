import pytest
from src_0346 import task_func
import pandas as pd
import seaborn as sns

# Test cases for the function
def test_task_func():
    # Create a sample DataFrame
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Test case 1: Valid input
    ax = task_func(df, 'col1', 'col2')
    assert ax is not None, "The plot should be created"

    # Test case 2: Invalid DataFrame
    with pytest.raises(ValueError):
        task_func(None, 'col1', 'col2')

    # Test case 3: Invalid column
    with pytest.raises(ValueError):
        task_func(df, 'nonexistent_col1', 'col2')

    # Test case 4: Invalid DataFrame
    with pytest.raises(ValueError):
        task_func('invalid_df', 'col1', 'col2')

    # Test case 5: Empty DataFrame
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(empty_df, 'col1', 'col2')