import pytest
from src_0551 import task_func
from collections import Counter
import pandas as pd

def test_task_func():
    # Test case 1
    list_of_menuitems = [['apple', 'banana', 'apple'], ['banana', 'orange', 'banana']]
    expected_output = pd.DataFrame({
        'MenuItem': ['apple', 'banana', 'orange'],
        'Count': [2, 3, 1]
    })
    expected_output.set_index('MenuItem', inplace=True)
    
    result = task_func(list_of_menuitems)
    pd.testing.assert_frame_equal(result, expected_output)

    # Add more test cases as needed