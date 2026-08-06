python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src_0554 import task_func

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Test case 1: Both lists are empty
    a = []
    b = []
    ax = task_func(a, b)
    assert ax.get_figure().axes == []
    
    # Test case 2: a is empty, b is not empty
    a = []
    b = [1, 2, 3]
    ax = task_func(a, b)
    assert ax.get_figure().axes == []
    
    # Test case 3: a is not empty, b is empty
    a = [1, 2, 3]
    b = []
    ax = task_func(a, b)
    assert ax.get_figure().axes == []
    
    # Test case 4: a and b are not empty
    a = [1, 2, 3]
    b = [4, 5, 6]
    ax = task_func(a, b)
    assert ax.get_figure().axes != []