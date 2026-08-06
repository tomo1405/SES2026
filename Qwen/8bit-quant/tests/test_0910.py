import pytest
from src_0910 import task_func
import pandas as pd

def test_task_func_default_input():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 27  # 9 letters * 3 categories
    assert set(df['Letter'].unique()) == set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    assert set(df['Category'].unique()) == set(['Category 1', 'Category 2', 'Category 3'])

def test_task_func_custom_letters_and_categories():
    letters = ['X', 'Y', 'Z']
    categories = ['Cat 1', 'Cat 2']
    df = task_func(letters=letters, categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 6  # 3 letters * 2 categories
    assert set(df['Letter'].unique()) == set(['X', 'Y', 'Z'])
    assert set(df['Category'].unique()) == set(['Cat 1', 'Cat 2'])

def test_task_func_single_category():
    categories = ['Single Category']
    df = task_func(categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 9  # 9 letters * 1 category
    assert set(df['Letter'].unique()) == set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    assert set(df['Category'].unique()) == set(['Single Category'])

def test_task_func_single_letter():
    letters = ['A']
    df = task_func(letters=letters)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3  # 1 letter * 3 categories
    assert set(df['Letter'].unique()) == set(['A'])
    assert set(df['Category'].unique()) == set(['Category 1', 'Category 2', 'Category 3'])

def test_task_func_empty_letters():
    with pytest.raises(ValueError):
        task_func(letters=[])

def test_task_func_empty_categories():
    with pytest.raises(ValueError):
        task_func(categories=[])