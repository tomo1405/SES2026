import pandas as pd
from src_0910 import task_func


def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'Letter' in df.columns
    assert 'Category' in df.columns
    assert len(df) == len(letters) * len(categories)

def test_task_func_custom_letters_and_categories():
    letters = ['A', 'B', 'C', 'D', 'E']
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    df = task_func(letters=letters, categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert 'Letter' in df.columns
    assert 'Category' in df.columns
    assert len(df) == len(letters) * len(categories)