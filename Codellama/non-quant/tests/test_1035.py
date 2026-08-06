import pandas as pd
from src_1035 import task_func


def test_task_func():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 0.0

def test_task_func_with_different_sales():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 0.0

def test_task_func_with_empty_sales():
    s1 = pd.Series([], index=CATEGORIES)
    s2 = pd.Series([], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0.0

def test_task_func_with_different_categories():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 0.0