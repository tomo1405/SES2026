import pandas as pd
from src_0172 import task_func


def test_task_func_returns_dataframe():
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert isinstance(statistics_df, pd.DataFrame)

def test_task_func_returns_correct_columns():
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert set(statistics_df.columns) == {'Count', 'Percentage'}

def test_task_func_returns_correct_values():
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert statistics_df.loc['Carrot', 'Count'] == 10
    assert statistics_df.loc['Potato', 'Count'] == 10
    assert statistics_df.loc['Tomato', 'Count'] == 10
    assert statistics_df.loc['Cabbage', 'Count'] == 10
    assert statistics_df.loc['Spinach', 'Count'] == 10
    assert statistics_df.loc['Carrot', 'Percentage'] == 20
    assert statistics_df.loc['Potato', 'Percentage'] == 20
    assert statistics_df.loc['Tomato', 'Percentage'] == 20
    assert statistics_df.loc['Cabbage', 'Percentage'] == 20
    assert statistics_df.loc['Spinach', 'Percentage'] == 20

def test_task_func_returns_correct_values_with_seed():
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict, seed=123)
    assert statistics_df.loc['Carrot', 'Count'] == 10
    assert statistics_df.loc['Potato', 'Count'] == 10
    assert statistics_df.loc['Tomato', 'Count'] == 10
    assert statistics_df.loc['Cabbage', 'Count'] == 10
    assert statistics_df.loc['Spinach', 'Count'] == 10
    assert statistics_df.loc['Carrot', 'Percentage'] == 20
    assert statistics_df.loc['Potato', 'Percentage'] == 20
    assert statistics_df.loc['Tomato', 'Percentage'] == 20
    assert statistics_df.loc['Cabbage', 'Percentage'] == 20
    assert statistics_df.loc['Spinach', 'Percentage'] == 20

def test_task_func_returns_correct_values_with_different_vegetable_dict():
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert statistics_df.loc['Carrot', 'Count'] == 10
    assert statistics_df.loc['Potato', 'Count'] == 10
    assert statistics_df.loc['Tomato', 'Count'] == 10
    assert statistics_df.loc['Cabbage', 'Count'] == 10
    assert statistics_df.loc['Spinach', 'Count'] == 10
    assert statistics_df.loc['Carrot', 'Percentage'] == 20
    assert statistics_df.loc['Potato', 'Percentage'] == 20
    assert statistics_df.loc['Tomato', 'Percentage'] == 20
    assert statistics_df.loc['Cabbage', 'Percentage'] == 20
    assert statistics_df.loc['Spinach', 'Percentage'] == 20