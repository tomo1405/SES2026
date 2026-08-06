import pytest
from src_0053 import task_func

def test_task_func_no_text():
    result = task_func("")
    assert result.empty

def test_task_func_only_stopwords():
    result = task_func("a an the in is are")
    assert result.empty

def test_task_func_single_word():
    result = task_func("hello")
    assert result.equals(pd.Series([1], index=["hello"]))

def test_task_func_multiple_words():
    result = task_func("hello world hello")
    assert result.equals(pd.Series([2], index=["hello"]).append(pd.Series([1], index=["world"])))

def test_task_func_case_insensitivity():
    result = task_func("Hello HELLO hello")
    assert result.equals(pd.Series([3], index=["hello"]))

def test_task_func_with_punctuation():
    result = task_func("Hello, world! Hello.")
    assert result.equals(pd.Series([2], index=["hello"]).append(pd.Series([1], index=["world"])))

def test_task_func_with_numbers():
    result = task_func("Hello 123 world")
    assert result.equals(pd.Series([1], index=["hello"]).append(pd.Series([1], index=["world"])))