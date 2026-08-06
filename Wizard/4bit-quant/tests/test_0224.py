python
import pandas as pd
import pytest
from src_0224 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    dct = {'a': 1, 'b': 2, 'c': 3}
    columns = ['B']
    expected_result = pd.DataFrame({'A': [-1.41421356, 0.0, 1.41421356], 'B': [0, 1, 2]})
    result = task_func(df, dct, columns)
    assert result.equals(expected_result)

    # Test case 2: Invalid input (df is not a DataFrame)
    with pytest.raises(ValueError):
        task_func('not a DataFrame', dct, columns)

    # Test case 3: Invalid input (dct contains non-string keys)
    with pytest.raises(ValueError):
        task_func(df, {1: 1, 2: 2, 3: 3}, columns)

    # Test case 4: Invalid input (columns contains non-string values)
    with pytest.raises(ValueError):
        task_func(df, dct, ['A', 1])

    # Test case 5: Invalid input (columns contains non-existent column)
    with pytest.raises(ValueError):
        task_func(df, dct, ['A', 'C'])

    # Test case 6: Invalid input (columns contains numerical column)
    with pytest.raises(ValueError):
        task_func(df, dct, ['A', 'B', 1])

    # Test case 7: Invalid input (columns contains non-categorical column)
    with pytest.raises(ValueError):
        task_func(df, dct, ['A', 'B', 'C'])