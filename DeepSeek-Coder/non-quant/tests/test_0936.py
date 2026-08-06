import pytest
from src_0936 import task_func
import pandas as pd

def test_empty_word():
    result = task_func("")
    expected = pd.DataFrame({'Letter': [], 'Position': []})
    pd.testing.assert_frame_equal(result, expected)

def test_invalid_input():
    with pytest.raises(ValueError):
        task_func("a1b2")

def test_valid_input():
    result = task_func("abc")
    expected = pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})
    pd.testing.assert_frame_equal(result, expected)