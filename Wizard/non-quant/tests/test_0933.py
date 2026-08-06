python
import pytest
from src_0933 import task_func

def test_task_func():
    # Test case 1: word with no alphabetic characters
    assert task_func('12345') == []
    
    # Test case 2: word with only one alphabetic character
    assert task_func('a') == []
    
    # Test case 3: word with two alphabetic characters
    assert task_func('ab') == [('a', 'b')]
    
    # Test case 4: word with three alphabetic characters
    assert task_func('abc') == [('ab', 1)]
    
    # Test case 5: word with four alphabetic characters
    assert task_func('abcd') == [('ab', 1)]
    
    # Test case 6: word with five alphabetic characters
    assert task_func('abcde') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1)]
    
    # Test case 7: word with six alphabetic characters
    assert task_func('abcdef') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1)]