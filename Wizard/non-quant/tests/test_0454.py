python
import re
import string
from random import choice
import pytest

def task_func(n, pattern):
    while True:
        s = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, s):
            return s

def test_task_func():
    # Test case 1
    assert task_func(5, r'[a-z]{5}') == 'yekkz'
    
    # Test case 2
    assert task_func(10, r'[a-z]{10}') == 'yekkzqnbw'
    
    # Test case 3
    assert task_func(15, r'[a-z]{15}') == 'yekkzqnbwrx'
    
    # Test case 4
    assert task_func(20, r'[a-z]{20}') == 'yekkzqnbwrxjgz'
    
    # Test case 5
    assert task_func(25, r'[a-z]{25}') == 'yekkzqnbwrxjgzv'
    
    # Test case 6
    assert task_func(30, r'[a-z]{30}') == 'yekkzqnbwrxjgzvpm'
    
    # Test case 7
    assert task_func(35, r'[a-z]{35}') == 'yekkzqnbwrxjgzvpmf'
    
    # Test case 8
    assert task_func(40, r'[a-z]{40}') == 'yekkzqnbwrxjgzvpmfhs'
    
    # Test case 9
    assert task_func(45, r'[a-z]{45}') == 'yekkzqnbwrxjgzvpmfhsb'
    
    # Test case 10
    assert task_func(50, r'[a-z]{50}') == 'yekkzqnbwrxjgzvpmfhsbmn'