import pytest
from src_0343 import task_func

def test_task_func():
    # Test with empty list
    elements = []
    pattern = r'\w+'
    result = task_func(elements, pattern)
    assert result == ([], False)

    # Test with non-empty list and pattern match
    elements = ['abc', 'def']
    pattern = r'[a-zA-Z]+'
    result = task_func(elements, pattern)
    assert len(result[0]) == 2
    assert all(isinstance(x, str) for x in result[0])
    assert result[1] is True

    # Test with non-empty list and no pattern match
    elements = ['123', '456']
    pattern = r'[a-zA-Z]+'
    result = task_func(elements, pattern)
    assert len(result[0]) == 2
    assert all(isinstance(x, str) for x in result[0])
    assert result[1] is False

    # Test with different seed
    elements = ['ghi', 'jkl']
    pattern = r'[a-zA-Z]+'
    result1 = task_func(elements, pattern, seed=100)
    result2 = task_func(elements, pattern, seed=200)
    assert result1 != result2

    # Test with special characters in elements
    elements = ['!@#', '$%^']
    pattern = r'[a-zA-Z]+'
    result = task_func(elements, pattern)
    assert len(result[0]) == 2
    assert all(isinstance(x, str) for x in result[0])
    assert result[1] is True

    # Test with pattern that matches part of the string
    elements = ['mno', 'pqr']
    pattern = r'no'
    result = task_func(elements, pattern)
    assert len(result[0]) == 2
    assert all(isinstance(x, str) for x in result[0])
    assert result[1] is True

    # Test with pattern that does not match
    elements = ['stu', 'vwx']
    pattern = r'xyz'
    result = task_func(elements, pattern)
    assert len(result[0]) == 2
    assert all(isinstance(x, str) for x in result[0])
    assert result[1] is False