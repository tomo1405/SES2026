import pandas as pd
import pytest
import string

from src_0936 import task_func

def test_task_func():
    # Test case 1: Empty input word
    expected_df = pd.DataFrame({'Letter': [], 'Position': []})
    actual_df = task_func('')
    assert actual_df.equals(expected_df)

    # Test case 2: Input word with invalid characters
    with pytest.raises(ValueError) as exc_info:
        task_func('123')
    assert 'Input word must be in lowercase alphabetic characters only.' in str(exc_info.value)

    # Test case 3: Valid input word
    word = 'python'
    expected_df = pd.DataFrame({'Letter': list(word), 'Position': [26, 16, 1, 19, 14, 4]})
    actual_df = task_func(word)
    assert actual_df.equals(expected_df)