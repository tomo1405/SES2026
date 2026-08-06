import pandas as pd
import numpy as np
from src_0150 import task_func

def test_task_func():
    elements = ['apple', 'banana', 'cherry']
    expected_output = pd.DataFrame({
        'Element': ['apple', 'banana', 'cherry'],
        'Count': [5, 6, 6]
    })
    actual_output = task_func(elements)
    assert actual_output.equals(expected_output)

def test_task_func_with_index():
    elements = ['apple', 'banana', 'cherry']
    expected_output = pd.DataFrame({
        'Index': [0, 1, 2],
        'Element': ['apple', 'banana', 'cherry'],
        'Count': [5, 6, 6]
    })
    actual_output = task_func(elements, include_index=True)
    assert actual_output.equals(expected_output)