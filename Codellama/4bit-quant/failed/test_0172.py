import pytest
from src_0172 import task_func

def test_task_func():
    # Test with a dictionary of vegetables
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    result = task_func(vegetable_dict)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different dictionary of vegetables
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    result = task_func(vegetable_dict, seed=1234)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different seed
    result = task_func(vegetable_dict, seed=4321)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different dictionary of vegetables
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    result = task_func(vegetable_dict, seed=1234)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different seed
    result = task_func(vegetable_dict, seed=4321)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different dictionary of vegetables
    vegetable_dict = {'Carrot': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Fruit', 'Cabbage': 'Vegetable', 'Spinach': 'Vegetable'}
    result = task_func(vegetable_dict, seed=1234)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))

    # Test with a different seed
    result = task_func(vegetable_dict, seed=4321)
    assert result.equals(pd.DataFrame({'Count': [10, 10, 10, 10, 10], 'Percentage': [20, 20, 20, 20, 20]}, index=['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']))