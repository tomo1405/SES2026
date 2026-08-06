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

def test_task_func_default_args():
    df = task_func()
    assert df['Letter'].unique().tolist() == letters
    assert df['Category'].unique().tolist() == categories

def test_task_func_custom_args():
    custom_letters = ['X', 'Y', 'Z']
    custom_categories = ['Category 4', 'Category 5', 'Category 6']
    df = task_func(letters=custom_letters, categories=custom_categories)
    assert df['Letter'].unique().tolist() == custom_letters
    assert df['Category'].unique().tolist() == custom_categories