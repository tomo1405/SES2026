python
import pandas as pd
import numpy as np
import pytest

from src_1035 import task_func

@pytest.fixture
def sales_data():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 250, 350, 450, 550], index=CATEGORIES)
    return s1, s2

def test_task_func(sales_data):
    s1, s2 = sales_data
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 50.0

def test_task_func_no_high_sales_categories(sales_data):
    s1, s2 = sales_data
    s1.iloc[0] = 10
    s2.iloc[0] = 10
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0.0

def test_task_func_all_low_sales_categories(sales_data):
    s1, s2 = sales_data
    s1.iloc[1:] = 10
    s2.iloc[1:] = 10
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0.0