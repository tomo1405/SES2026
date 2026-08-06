python
import re
import collections
import pytest

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):

    if not isinstance(string, str):
        raise TypeError("Input string should be of type string.")

    if not isinstance(patterns, list):
        raise TypeError("patterns should be a list of strings.")
    
    if not all(isinstance(s, str) for s in patterns):
        raise TypeError("patterns should be a list of strings.")

    

    pattern_counts = collections.defaultdict(int)

    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))

    return dict(pattern_counts)

def test_task_func():
    # Test case 1
    assert task_func('nnn aaa sss ddd fff') == {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}

    # Test case 2
    assert task_func('nnn aaa sss ddd fff', ['nnn', 'aaa', 'sss', 'ddd', 'fff']) == {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}

    # Test case 3
    assert task_func('nnn aaa sss ddd fff', ['nnn', 'aaa', 'sss', 'ddd', 'fff', 'ggg']) == {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1, 'ggg': 0}

    # Test case 4
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 5
    with pytest.raises(TypeError):
        task_func('nnn aaa sss ddd fff', 'nnn')

    # Test case 6
    with pytest.raises(TypeError):
        task_func('nnn aaa sss ddd fff', ['nnn', 'aaa', 'sss', 'ddd', 123])

    # Test case 7
    with pytest.raises(TypeError):
        task_func('nnn aaa sss ddd fff', ['nnn', 'aaa', 'sss', 'ddd', 'fff', 123])