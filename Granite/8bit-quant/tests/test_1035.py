import pandas as pd
import numpy as np
import pytest
from src_1035 import task_func

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def test_task_func():
    s1 = pd.Series([100, 250, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 200, 350, 380, 490], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance > 0

def test_task_func_no_high_sales():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 200, 350, 380, 490], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0

def test_task_func_edit_distance():
    s1 = pd.Series([100, 250, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 200, 350, 380, 490], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    expected_edit_distance = np.linalg.norm(s1 - s2)
    assert edit_distance == expected_edit_distance