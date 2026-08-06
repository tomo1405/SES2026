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
    
    # Test case 4: word with multiple pairs of alphabetic characters
    assert task_func('aabbbcc') == [('a', 'b'), ('b', 'b'), ('b', 'c')]
    
    # Test case 5: word with multiple pairs of alphabetic characters and non-alphabetic characters
    assert task_func('aabbbcc123') == [('a', 'b'), ('b', 'b'), ('b', 'c')]