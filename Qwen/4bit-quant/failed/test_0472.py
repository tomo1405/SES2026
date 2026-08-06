import pytest
from src_0472 import task_func

def test_task_func_with_empty_list():
    assert task_func([]).empty

def test_task_func_with_single_word():
    result = task_func(["Hello"])
    assert result.index[0] == "hello"
    assert result.loc["hello", "Count"] == 1

def test_task_func_with_multiple_words():
    result = task_func(["Hello", "world", "HELLO", "WORLD", "hello"])
    assert result.index.tolist() == ["hello", "world"]
    assert result.loc["hello", "Count"] == 3
    assert result.loc["world", "Count"] == 2

def test_task_func_with_whitespace():
    result = task_func(["   Hello   ", "\tworld\n", "  hello  "])
    assert result.index.tolist() == ["hello", "world"]
    assert result.loc["hello", "Count"] == 2
    assert result.loc["world", "Count"] == 1

def test_task_func_with_mixed_case():
    result = task_func(["MixedCase", "MIXEDCASE", "mixedcase"])
    assert result.index[0] == "mixedcase"
    assert result.loc["mixedcase", "Count"] == 3

def test_task_func_with_special_characters():
    result = task_func(["!@#Hello!@#", "!@#hello!@#"])
    assert result.index[0] == "hello"
    assert result.loc["hello", "Count"] == 2