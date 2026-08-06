import pytest
from src_0910 import task_func
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 27  # 9 letters * 3 categories
    assert all(df['Letter'].isin(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']))
    assert all(df['Category'].isin(['Category 1', 'Category 2', 'Category 3']))

def test_task_func_custom_letters():
    df = task_func(letters=['X', 'Y', 'Z'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 9  # 3 letters * 3 categories
    assert all(df['Letter'].isin(['X', 'Y', 'Z']))
    assert all(df['Category'].isin(['Category 1', 'Category 2', 'Category 3']))

def test_task_func_custom_categories():
    df = task_func(categories=['Cat 1', 'Cat 2'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 18  # 9 letters * 2 categories
    assert all(df['Letter'].isin(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']))
    assert all(df['Category'].isin(['Cat 1', 'Cat 2']))

def test_task_func_custom_letters_and_categories():
    df = task_func(letters=['P', 'Q'], categories=['Group A', 'Group B'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4  # 2 letters * 2 categories
    assert all(df['Letter'].isin(['P', 'Q']))
    assert all(df['Category'].isin(['Group A', 'Group B']))

def test_task_func_empty_letters():
    with pytest.raises(ValueError):
        task_func(letters=[])

def test_task_func_empty_categories():
    with pytest.raises(ValueError):
        task_func(categories=[])

def test_task_func_single_letter():
    df = task_func(letters=['L'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3  # 1 letter * 3 categories
    assert all(df['Letter'] == 'L')
    assert all(df['Category'].isin(['Category 1', 'Category 2', 'Category 3']))

def test_task_func_single_category():
    df = task_func(categories=['Single Category'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 9  # 9 letters * 1 category
    assert all(df['Letter'].isin(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']))
    assert all(df['Category'] == 'Single Category')