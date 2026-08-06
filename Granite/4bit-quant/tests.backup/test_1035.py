import pandas as pd
import numpy as np
import pytest
from src_1035 import task_func

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def test_task_func():
    # Test case 1: No categories meet the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 250, 350, 450, 550], index=CATEGORIES)
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 2: One category meets the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 250, 350, 450, 200], index=CATEGORIES)
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 3: Two categories meet the sales threshold
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 250, 350, 200, 100], index=CATEGORIES)
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output

    # Test case 4: All categories meet the sales threshold
    s1 = pd.Series([300, 400, 500, 600, 700], index=CATEGORIES)
    s2 = pd.Series([350, 450, 550, 650, 750], index=CATEGORIES)
    expected_output = (None, 0.0)
    actual_output = task_func(s1, s2)
    assert actual_output == expected_output