python
import pytest
from src_0136 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_ax = None
    actual_df, actual_ax = task_func(df)
    assert actual_df.equals(expected_df)
    assert actual_ax == expected_ax

    # Test case 2: Empty input
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 3: Non-dataframe input
    with pytest.raises(ValueError):
        task_func(123)