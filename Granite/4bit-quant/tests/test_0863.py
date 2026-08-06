import pytest
from src_0863 import task_func

def test_task_func():
    n = 10
    seed = 42
    expected_output = {'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
                       'b': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 
                       'c': ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'], 
                       'd': ['d', 'd', 'd', 'd', 'd', 'd', 'd'], 
                       'e': ['e', 'e', 'e', 'e', 'e', 'e'], 
                       'f': ['f', 'f', 'f', 'f', 'f'], 
                       'g': ['g', 'g', 'g', 'g'], 
                       'h': ['h', 'h', 'h'], 
                       'i': ['i', 'i'], 
                       'j': ['j']}
    
    actual_output = task_func(n, seed)
    
    assert actual_output == expected_output