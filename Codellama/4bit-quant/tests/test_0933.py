import pytest
from src_0933 import task_func

def test_task_func():
    # Test case 1: empty input
    assert task_func("") == []
    
    # Test case 2: single letter input
    assert task_func("a") == []
    
    # Test case 3: multiple letters input
    assert task_func("hello") == [('he', 1)]
    
    # Test case 4: multiple letters input with duplicates
    assert task_func("hellohello") == [('he', 2)]
    
    # Test case 5: multiple letters input with duplicates and non-duplicates
    assert task_func("hellohelloworld") == [('he', 2), ('wo', 1)]