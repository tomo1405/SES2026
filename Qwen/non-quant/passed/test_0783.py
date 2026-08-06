import pytest
from src_0783 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_parameters():
    n = 5
    df = task_func(n)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n
    assert all(col in df.columns for col in ['title', 'title_url', 'id', 'category', 'views'])

def test_task_func_custom_domain_and_categories():
    n = 3
    domain = "testsite.com"
    categories = ['Education', 'Entertainment']
    df = task_func(n, domain=domain, categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n
    assert all(col in df.columns for col in ['title', 'title_url', 'id', 'category', 'views'])
    assert all(df['title_url'].str.startswith(domain))
    assert all(df['category'].isin(categories))

def test_task_func_random_seed():
    n = 4
    random_seed = 42
    df1 = task_func(n, random_seed=random_seed)
    df2 = task_func(n, random_seed=random_seed)
    assert df1.equals(df2)

def test_task_func_zero_articles():
    n = 0
    df = task_func(n)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n

def test_task_func_large_n():
    n = 100
    df = task_func(n)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n
    assert all(isinstance(view, int) for view in df['views'])

def test_task_func_views_distribution():
    n = 1000
    df = task_func(n)
    views = df['views']
    mean_views = np.mean(views)
    std_views = np.std(views)
    # Check if the mean is close to the expected value of a Poisson distribution with lambda=1000
    assert np.isclose(mean_views, 1000, atol=50)
    # Check if the standard deviation is close to the expected value of a Poisson distribution with lambda=1000
    assert np.isclose(std_views, np.sqrt(1000), atol=50)