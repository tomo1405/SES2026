import pytest
from src_0767 import task_func

def test_task_func_default_patterns():
    input_string = "nnn aaa sss ddd fff"
    expected_output = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    assert task_func(input_string) == expected_output

def test_task_func_custom_patterns():
    input_string = "abcabcabc"
    patterns = ['abc', 'bca', 'cab']
    expected_output = {'abc': 3, 'bca': 0, 'cab': 0}
    assert task_func(input_string, patterns) == expected_output

def test_task_func_no_matches():
    input_string = "xyz"
    expected_output = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
    assert task_func(input_string) == expected_output

def test_task_func_empty_string():
    input_string = ""
    expected_output = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
    assert task_func(input_string) == expected_output

def test_task_func_non_string_input():
    with pytest.raises(TypeError, match="Input string should be of type string."):
        task_func(123)

def test_task_func_non_list_patterns():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", "not a list")

def test_task_func_patterns_with_non_strings():
    with pytest.raises(TypeError, match="patterns should be a list of strings."):
        task_func("test", [123, "valid"])