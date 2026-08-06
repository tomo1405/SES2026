import pytest
import pandas as pd
from src_0178 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({"Title": ["This is a title"], "Content": ["This is a content"]})
    result = task_func(df)
    assert isinstance(result, dict)

def test_task_func_invalid_input():
    df = pd.DataFrame({"Title": ["This is a title"], "Content": ["This is a content"]})
    df = df.drop("Title", axis=1)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_empty_input():
    df = pd.DataFrame({"Title": [], "Content": []})
    result = task_func(df)
    assert result == {}

def test_task_func_interesting_articles():
    df = pd.DataFrame({"Title": ["This is a title", "This is another title"], "Content": ["This is a content", "This is another content"]})
    result = task_func(df)
    assert isinstance(result, dict)

def test_task_func_punctuation():
    df = pd.DataFrame({"Title": ["This is a title"], "Content": ["This, is a content"]})
    result = task_func(df)
    assert result == {"This": 1, "is": 1, "a": 1, "content": 1}