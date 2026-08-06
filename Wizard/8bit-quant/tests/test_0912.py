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
    letters = "JKL"
    expected_result = 40353
    assert task_func(letters) == expected_result
    
    # Test case 5
    letters = "MNO"
    expected_result = 129600
    assert task_func(letters) == expected_result
    
    # Test case 6
    letters = "PQR"
    expected_result = 3628800
    assert task_func(letters) == expected_result
    
    # Test case 7
    letters = "STU"
    expected_result = 871782911
    assert task_func(letters) == expected_result
    
    # Test case 8
    letters = "VWXYZ"
    expected_result = 39916800
    assert task_func(letters) == expected_result