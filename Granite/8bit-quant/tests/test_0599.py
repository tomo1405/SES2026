import pandas as pd
import pytest

from src_0599 import task_func

def test_task_func():
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
    letter = 'b'
    expected_output = {5: 2}

    actual_output = task_func(df, letter)

    assert actual_output == expected_output

def test_task_func_with_empty_df():
    df = {'Word': []}
    letter = 'b'
    expected_output = {}

    actual_output = task_func(df, letter)

    assert actual_output == expected_output

def test_task_func_with_non_string_column():
    df = {'Word': [1, 2, 3]}
    letter = 'b'

    with pytest.raises(TypeError):
        task_func(df, letter)