import pytest
from src_1026 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_input():
    data_dict = {}
    df, ax = task_func(data_dict)
    assert df.empty
    assert ax.get_title() == "Scaled Values"

def test_task_func_no_missing_values():
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert all(df['A'] >= 0) and all(df['A'] <= 1)
    assert all(df['B'] >= 0) and all(df['B'] <= 1)

def test_task_func_with_missing_values():
    data_dict = {'A': [1, None, 3], 'B': [4, 5, None]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert len(df) == 1
    assert all(df['A'] >= 0) and all(df['A'] <= 1)
    assert all(df['B'] >= 0) and all(df['B'] <= 1)

def test_task_func_single_value():
    data_dict = {'A': [1, 1, 1], 'B': [2, 2, 2]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert df['A'].unique()[0] == 0
    assert df['B'].unique()[0] == 0

def test_task_func_different_scales():
    data_dict = {'A': [1, 2, 3], 'B': [100, 200, 300]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert all(df['A'] >= 0) and all(df['A'] <= 1)
    assert all(df['B'] >= 0) and all(df['B'] <= 1)