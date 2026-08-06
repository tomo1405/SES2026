import pytest
from src_0767 import task_func

def test_task_func_valid_input():
    result = task_func("nnn aaa sss ddd fff")
    assert result == {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}

def test_task_func_no_matches():
    result = task_func("no matches here")
    assert result == {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}

def test_task_func_empty_string():
    result = task_func("")
    assert result == {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}

def test_task_func_custom_patterns():
    result = task_func("abc abc abc", patterns=['abc', 'def'])
    assert result == {'abc': 3, 'def': 0}

def test_task_func_non_string_input():
    with pytest.raises(TypeError, match="Input string should be of type string."):
        task_func(123)

def test_task_func_non_list_patterns():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", patterns="not a list")

def test_task_func_non_string_patterns():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", patterns=[123, "string"])