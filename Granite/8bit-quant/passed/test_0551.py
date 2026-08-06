import pytest
from collections import Counter
import pandas as pd
from src_0551 import task_func

def test_task_func():
    list_of_menuitems = [['Pizza', 'Pasta'], ['Pizza', 'Salad'], ['Pasta', 'Salad']]
    expected_df = pd.DataFrame({'Count': [2, 2, 2]}, index=pd.Index(['Pizza', 'Pasta', 'Salad'], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)

def test_task_func_empty_list():
    list_of_menuitems = []
    expected_df = pd.DataFrame({'Count': []}, index=pd.Index([], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)

def test_task_func_single_item():
    list_of_menuitems = [['Pizza']]
    expected_df = pd.DataFrame({'Count': [1]}, index=pd.Index(['Pizza'], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)

def test_task_func_multiple_counts():
    list_of_menuitems = [['Pizza', 'Pizza'], ['Pasta', 'Pasta', 'Pasta']]
    expected_df = pd.DataFrame({'Count': [2, 3]}, index=pd.Index(['Pizza', 'Pasta'], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)