import pandas as pd
import itertools
from random import shuffle
from src_0910 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'Letter' in df.columns
    assert 'Category' in df.columns
    assert len(df) == len(letters) * len(categories)

def test_task_func_letters():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    df = task_func(letters=letters)
    assert df['Letter'].unique().tolist() == letters

def test_task_func_categories():
    categories = ['Category 1', 'Category 2', 'Category 3']
    df = task_func(categories=categories)
    assert df['Category'].unique().tolist() == categories

def test_task_func_letters_categories():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    categories = ['Category 1', 'Category 2', 'Category 3']
    df = task_func(letters=letters, categories=categories)
    assert df['Letter'].unique().tolist() == letters
    assert df['Category'].unique().tolist() == categories