import pytest
from src_1035 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_high_sales():
    s1 = pd.Series([100, 150, 180, 250, 300], index=CATEGORIES)
    s2 = pd.Series([120, 170, 190, 240, 310], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0.0

def test_task_func_with_high_sales():
    s1 = pd.Series([100, 250, 180, 250, 300], index=CATEGORIES)
    s2 = pd.Series([120, 260, 190, 240, 310], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance > 0.0

def test_task_func_all_high_sales():
    s1 = pd.Series([210, 250, 280, 250, 300], index=CATEGORIES)
    s2 = pd.Series([220, 260, 290, 240, 310], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance > 0.0

def test_task_func_single_category_high_sales():
    s1 = pd.Series([100, 150, 180, 250, 300], index=CATEGORIES)
    s2 = pd.Series([120, 170, 190, 240, 310], index=CATEGORIES)
    s1["Electronics"] = 210
    s2["Electronics"] = 220
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance > 0.0

def test_task_func_identical_sales():
    s1 = pd.Series([210, 250, 280, 250, 300], index=CATEGORIES)
    s2 = pd.Series([210, 250, 280, 250, 300], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert isinstance(ax, pd.DataFrame.plot.SeriesPlotter)
    assert isinstance(edit_distance, float)
    assert edit_distance == 0.0