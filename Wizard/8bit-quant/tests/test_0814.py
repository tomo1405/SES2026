python
import pytest
from src_0814 import task_func

def test_task_func():
    # Test case 1
    number_list = [1, 2, 3, 4, 5]
    element = 6
    expected_result = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]})
    assert task_func(number_list, element).equals(expected_result)
    
    # Test case 2
    number_list = [1, 2, 3, 4, 5]
    element = 15
    expected_result = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), (1, 2, 6), (1, 3, 6), (1, 4, 6), (1, 5, 6), (2, 3, 6), (2, 4, 6), (2, 5, 6), (3, 4, 6), (3, 5, 6), (4, 5, 6)]})
    assert task_func(number_list, element).equals(expected_result)
    
    # Test case 3
    number_list = [1, 2, 3, 4, 5]
    element = 10
    expected_result = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]})
    assert task_func(number_list, element).equals(expected_result)
    
    # Test case 4
    number_list = [1, 2, 3, 4, 5]
    element = 0
    expected_result = pd.DataFrame({'Combinations': []})
    assert task_func(number_list, element).equals(expected_result)
    
    # Test case 5
    number_list = [1, 2, 3, 4, 5]
    element = 1
    expected_result = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]})
    assert task_func(number_list, element).equals(expected_result)
    
    # Test case 6
    number_list = [1, 2, 3, 4, 5]
    element = 100
    expected_result = pd.DataFrame({'Combinations': []})
    assert task_func(number_list, element).equals(expected_result)