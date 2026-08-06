python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0141 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 'B']
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, 0.4472135954999579, 1.3416407864998738],
                                'B': [-1.3416407864998738, 0.4472135954999579, 1.3416407864998738]})
    result_df = task_func(df, cols)
    assert result_df.equals(expected_df)

    # Test case 2: Invalid input: df is not a DataFrame
    with pytest.raises(ValueError):
        task_func(123, cols)

    # Test case 3: Invalid input: cols is not a list of strings
    with pytest.raises(ValueError):
        task_func(df, 123)

    # Test case 4: Invalid input: cols contains a non-existent column
    with pytest.raises(ValueError):
        task_func(df, ['A', 'C'])