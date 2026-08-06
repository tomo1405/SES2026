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
    expected_result = 120
    assert task_func(letters) == expected_result
    
    # Test case 3
    letters = "GHI"
    expected_result = 362880
    assert task_func(letters) == expected_result
    
    # Test case 4
    letters = "JKL"
    expected_result = 15625
    assert task_func(letters) == expected_result
    
    # Test case 5
    letters = "MNO"
    expected_result = 20922789888000
    assert task_func(letters) == expected_result
    
    # Test case 6
    letters = "PQR"
    expected_result = 1048576
    assert task_func(letters) == expected_result
    
    # Test case 7
    letters = "STU"
    expected_result = 1306367456
    assert task_func(letters) == expected_result
    
    # Test case 8
    letters = "VWX"
    expected_result = 129060192
    assert task_func(letters) == expected_result
    
    # Test case 9
    letters = "YZ"
    expected_result = 15
    assert task_func(letters) == expected_result