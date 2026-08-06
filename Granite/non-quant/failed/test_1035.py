import pandas as pd
import numpy as np
from src_1035 import task_func

def test_task_func():
    # Test case 1: No categories meet the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500])
    s2 = pd.Series([100, 200, 300, 400, 500])
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 2: One category meets the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500])
    s2 = pd.Series([100, 200, 300, 400, 600])
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 3: Two categories meet the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500])
    s2 = pd.Series([100, 200, 300, 500, 600])
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 4: Three categories meet the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500])
    s2 = pd.Series([100, 200, 400, 500, 600])
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 5: All categories meet the sales threshold
    s1 = pd.Series([300, 400, 500, 600, 700])
    s2 = pd.Series([300, 400, 500, 600, 700])
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output