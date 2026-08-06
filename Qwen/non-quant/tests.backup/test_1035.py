import pytest
from src_1035 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_high_sales():
    s1 = pd.Series([150, 180, 250, 300, 190], index=CATEGORIES)
    s2 = pd.Series([210, 170, 260, 290, 180], index=CATEGORIES)
    result = task_func(s1, s2)
    assert result == (None, 0.0)

def test_task_func_with_high_sales():
    s1 = pd.Series([250, 180, 250, 300, 190], index=CATEGORIES)
    s2 = pd.Series([210, 270, 260, 290, 180], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm(pd.Series([250, 250]) - pd.Series([210, 260]))

def test_task_func_all_categories_above_threshold():
    s1 = pd.Series([250, 280, 250, 300, 190], index=CATEGORIES)
    s2 = pd.Series([210, 270, 260, 290, 280], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm(pd.Series([250, 280, 250, 300, 190]) - pd.Series([210, 270, 260, 290, 280]))

def test_task_func_single_category_above_threshold():
    s1 = pd.Series([150, 180, 250, 300, 190], index=CATEGORIES)
    s2 = pd.Series([210, 170, 260, 290, 180], index=CATEGORIES)
    s1[CATEGORIES[0]] = 250
    s2[CATEGORIES[0]] = 210
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance == np.linalg.norm(pd.Series([250]) - pd.Series([210]))