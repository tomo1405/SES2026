python
import pytest
from src_0738 import task_func

def test_task_func():
    # Test case 1
    L = [1, 2, 3, 4, 5]
    expected_result = 3
    assert task_func(L) == expected_result
    
    # Test case 2
    L = [1, [2, 3], 4, [5, [6, 7]]]
    expected_result = 4
    assert task_func(L) == expected_result
    
    # Test case 3
    L = []
    with pytest.raises(ValueError):
        task_func(L)
    
    # Test case 4
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = 5.5
    assert task_func(L) == expected_result
    
    # Test case 5
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected_result = 6
    assert task_func(L) == expected_result