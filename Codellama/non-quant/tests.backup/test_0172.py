import pytest
from src_0172 import task_func

def test_task_func():
    # Test with a dictionary of vegetables
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert statistics_df.index.tolist() == ['Carrot', 'Potato', 'Cabbage', 'Spinach']
    assert statistics_df['Count'].tolist() == [1, 2, 3, 4]
    assert statistics_df['Percentage'].tolist() == [25, 50, 75, 100]

    # Test with a dictionary of vegetables and a seed
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    statistics_df = task_func(vegetable_dict, seed=123)
    assert statistics_df.index.tolist() == ['Carrot', 'Potato', 'Cabbage', 'Spinach']
    assert statistics_df['Count'].tolist() == [1, 2, 3, 4]
    assert statistics_df['Percentage'].tolist() == [25, 50, 75, 100]

    # Test with an empty dictionary
    vegetable_dict = {}
    statistics_df = task_func(vegetable_dict)
    assert statistics_df.empty

    # Test with a dictionary with only one key
    vegetable_dict = {'Carrot': 'Vegetable'}
    statistics_df = task_func(vegetable_dict)
    assert statistics_df.index.tolist() == ['Carrot']
    assert statistics_df['Count'].tolist() == [1]
    assert statistics_df['Percentage'].tolist() == [100]