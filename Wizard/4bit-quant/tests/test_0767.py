python
import pytest
from src_0767 import task_func

def test_task_func():
    # Test case 1
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff']
    expected_output = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    assert task_func(string, patterns) == expected_output

    # Test case 2
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff', 'ggg']
    expected_output = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1, 'ggg': 0}
    assert task_func(string, patterns) == expected_output

    # Test case 3
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff', '']
    expected_output = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    assert task_func(string, patterns) == expected_output

    # Test case 4
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff', 123]
    with pytest.raises(TypeError):
        task_func(string, patterns)

    # Test case 5
    string = 123
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff']
    with pytest.raises(TypeError):
        task_func(string, patterns)

    # Test case 6
    string = "nnn aaa sss ddd fff"
    patterns = 'nnn aaa sss ddd fff'
    with pytest.raises(TypeError):
        task_func(string, patterns)

    # Test case 7
    string = "nnn aaa sss ddd fff"
    patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff', 'nnn']
    expected_output = {'nnn': 2, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    assert task_func(string, patterns) == expected_output