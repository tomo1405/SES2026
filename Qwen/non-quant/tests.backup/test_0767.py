import pytest
from src_0767 import task_func

def test_task_func_with_default_patterns():
    result = task_func("nnn aaa sss ddd fff")
    assert result == {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}

def test_task_func_with_custom_patterns():
    result = task_func("hello world", ['lo', 'or'])
    assert result == {'lo': 3, 'or': 1}

def test_task_func_no_matches():
    result = task_func("abcde", ['xyz', 'uvw'])
    assert result == {'xyz': 0, 'uvw': 0}

def test_task_func_empty_string():
    result = task_func("")
    assert result == {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}

def test_task_func_non_string_input():
    with pytest.raises(TypeError, match="Input string should be of type string."):
        task_func(12345)

def test_task_func_non_list_patterns():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", "not a list")

def test_task_func_patterns_not_strings():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", [123, "valid"])