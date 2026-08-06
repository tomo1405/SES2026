import pytest
from src_0910 import task_func
import pandas as pd

def test_task_func_default():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Letter', 'Category']
    assert len(df) == 27  # 9 letters * 3 categories
    assert df['Letter'].unique().tolist() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    assert set(df['Category'].unique()) == {'Category 1', 'Category 2', 'Category 3'}

def test_task_func_custom_letters_and_categories():
    letters = ['X', 'Y', 'Z']
    categories = ['Cat 1', 'Cat 2']
    df = task_func(letters, categories)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Letter', 'Category']
    assert len(df) == 6  # 3 letters * 2 categories
    assert df['Letter'].unique().tolist() == ['X', 'Y', 'Z']
    assert set(df['Category'].unique()) == {'Cat 1', 'Cat 2'}

def test_task_func_single_category():
    df = task_func(categories=['Single Category'])
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Letter', 'Category']
    assert len(df) == 9  # 9 letters * 1 category
    assert df['Letter'].unique().tolist() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    assert df['Category'].unique().tolist() == ['Single Category']

def test_task_func_single_letter():
    df = task_func(letters=['L'])
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Letter', 'Category']
    assert len(df) == 3  # 1 letter * 3 categories
    assert df['Letter'].unique().tolist() == ['L']
    assert set(df['Category'].unique()) == {'Category 1', 'Category 2', 'Category 3'}

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func(letters=[], categories=['Category 1'])

    with pytest.raises(ValueError):
        task_func(letters=['A'], categories=[])

    with pytest.raises(ValueError):
        task_func(letters=[], categories=[])