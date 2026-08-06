import numpy as np
import pandas as pd
from src_1035 import task_func


def test_task_func_no_high_sales():
    s1 = pd.Series([150, 250, 300, 180, 220], index=CATEGORIES)
    s2 = pd.Series([160, 210, 290, 170, 230], index=CATEGORIES)
    result = task_func(s1, s2)
    assert result == (None, 0.0)

def test_task_func_with_high_sales():
    s1 = pd.Series([250, 250, 300, 180, 220], index=CATEGORIES)
    s2 = pd.Series([260, 210, 290, 170, 230], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm([10, 0, 0])

def test_task_func_all_high_sales():
    s1 = pd.Series([250, 250, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([260, 210, 290, 410, 510], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm([10, 0, 0, 10, 10])

def test_task_func_one_category_above_threshold():
    s1 = pd.Series([150, 250, 300, 180, 220], index=CATEGORIES)
    s2 = pd.Series([160, 210, 290, 170, 230], index=CATEGORIES)
    s1['Electronics'] = 250
    s2['Electronics'] = 260
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm([10])