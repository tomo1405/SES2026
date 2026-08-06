import pytest
from src_0839 import task_func

def test_task_func():
    import pandas as pd
    text_series = pd.Series(["Hello, World!", "This is a test."])
    expected_result = pd.Series(["hello world", "this is a test"])
    result = task_func(text_series)
    assert result.equals(expected_result)

def test_task_func_empty_text():
    import pandas as pd
    text_series = pd.Series([""])
    expected_result = pd.Series([""])
    result = task_func(text_series)
    assert result.equals(expected_result)

def test_task_func_null_text():
    import pandas as pd
    text_series = pd.Series([None])
    expected_result = pd.Series([None])
    result = task_func(text_series)
    assert result.equals(expected_result)