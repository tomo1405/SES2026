python
import pytest
from src_0933 import task_func

def test_task_func():
    # Test case 1: word with less than 2 alphabetic characters
    assert task_func('123') == []
    
    # Test case 2: word with 2 alphabetic characters
    assert task_func('ab') == [('a', 'b')]
    
    # Test case 3: word with 3 alphabetic characters
    assert task_func('abc') == [('ab', 1)]
    
    # Test case 4: word with 4 alphabetic characters
    assert task_func('abcd') == [('ab', 1), ('bc', 1), ('cd', 1)]
    
    # Test case 5: word with 5 alphabetic characters
    assert task_func('abcde') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1)]
    
    # Test case 6: word with 6 alphabetic characters
    assert task_func('abcdef') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1)]
    
    # Test case 7: word with 7 alphabetic characters
    assert task_func('abcdefg') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1), ('fg', 1)]
    
    # Test case 8: word with 8 alphabetic characters
    assert task_func('abcdefgh') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1), ('fg', 1), ('gh', 1)]
    
    # Test case 9: word with 9 alphabetic characters
    assert task_func('abcdefghi') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1), ('fg', 1), ('gh', 1), ('hi', 1)]
    
    # Test case 10: word with 10 alphabetic characters
    assert task_func('abcdefghij') == [('ab', 1), ('bc', 1), ('cd', 1), ('de', 1), ('ef', 1), ('fg', 1), ('gh', 1), ('hi', 1), ('ij', 1)]