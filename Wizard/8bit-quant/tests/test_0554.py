python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src_0554 import task_func

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Test case 1: Both lists are empty
    assert task_func([], []) is None
    
    # Test case 2: a is empty, b is not empty
    a = []
    b = [1, 2, 3]
    expected_ax = None
    actual_ax = task_func(a, b)
    assert expected_ax == actual_ax
    
    # Test case 3: a is not empty, b is empty
    a = [1, 2, 3]
    b = []
    expected_ax = None
    actual_ax = task_func(a, b)
    assert expected_ax == actual_ax
    
    # Test case 4: a and b are not empty
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected_ax = None
    actual_ax = task_func(a, b)
    assert expected_ax == actual_ax