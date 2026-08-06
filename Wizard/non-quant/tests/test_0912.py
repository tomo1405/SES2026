python
import pytest
from src_0912 import task_func

def test_task_func():
    # Test case 1
    letters = "ABC"
    expected_result = 6
    assert task_func(letters) == expected_result
    
    # Test case 2
    letters = "DEF"
    expected_result = 30
    assert task_func(letters) == expected_result
    
    # Test case 3
    letters = "GHI"
    expected_result = 729
    assert task_func(letters) == expected_result
    
    # Test case 4
    letters = "JKLMN"
    expected_result = 129600
    assert task_func(letters) == expected_result
    
    # Test case 5
    letters = "OPQRST"
    expected_result = 39916800
    assert task_func(letters) == expected_result
    
    # Test case 6
    letters = "UVWXYZ"
    expected_result = 129600
    assert task_func(letters) == expected_result