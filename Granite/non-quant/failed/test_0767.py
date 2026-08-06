import re
import collections
from src_0767 import task_func

def test_task_func_valid_input():
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff']
    expected_output = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    output = task_func(string, patterns)
    assert output == expected_output

def test_task_func_invalid_string_type():
    string = 123
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff']
    with pytest.raises(TypeError) as excinfo:
        task_func(string, patterns)
    assert "Input string should be of type string." in str(excinfo.value)

def test_task_func_invalid_patterns_type():
    string = "nnn aaa sss ddd fff"
    patterns = 'not a list'
    with pytest.raises(TypeError) as excinfo:
        task_func(string, patterns)
    assert "patterns should be a list of strings." in str(excinfo.value)

def test_task_func_invalid_pattern_type():
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 123, 'fff']
    with pytest.raises(TypeError) as excinfo:
        task_func(string, patterns)
    assert "patterns should be a list of strings." in str(excinfo.value)