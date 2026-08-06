import pytest
import pandas as pd
import numpy as np
from src_0783 import task_func

def test_task_func():
    n = 10
    df = task_func(n)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n
    assert 'title' in df.columns
    assert 'title_url' in df.columns
    assert 'id' in df.columns
    assert 'category' in df.columns
    assert 'views' in df.columns

def test_task_func_with_seed():
    n = 10
    random_seed = 42
    df1 = task_func(n, random_seed=random_seed)
    df2 = task_func(n, random_seed=random_seed)
    assert df1.equals(df2)

def test_task_func_with_category():
    n = 10
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    df = task_func(n, categories=categories)
    assert df['category'].isin(categories).all()

def test_task_func_with_domain():
    n = 10
    domain = "example.com"
    df = task_func(n, domain=domain)
    assert (df['title_url'].str.startswith(domain)).all()

def test_task_func_with_invalid_category():
    n = 10
    categories = ['Invalid', 'Category']
    with pytest.raises(ValueError):
        task_func(n, categories=categories)

def test_task_func_with_invalid_domain():
    n = 10
    domain = 123
    with pytest.raises(TypeError):
        task_func(n, domain=domain)