import numpy as np
import pandas as pd
from src_0783 import task_func


def test_task_func_output_type():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame), "The output should be a pandas DataFrame"

def test_task_func_number_of_rows():
    n = 10
    df = task_func(n)
    assert len(df) == n, f"The DataFrame should have {n} rows"

def test_task_func_columns():
    expected_columns = {'title', 'title_url', 'id', 'category', 'views'}
    df = task_func(5)
    assert set(df.columns) == expected_columns, "The DataFrame should have the correct columns"

def test_task_func_title_format():
    df = task_func(5)
    for i, row in df.iterrows():
        assert row['title'] == f"Article {i}", f"Incorrect title format for row {i}"

def test_task_func_title_url_format():
    df = task_func(5, domain="testsite.com")
    for i, row in df.iterrows():
        assert row['title_url'] == f"testsite.com/Article_{i}", f"Incorrect title_url format for row {i}"

def test_task_func_id_format():
    df = task_func(5)
    for i, row in df.iterrows():
        assert row['id'] == i, f"Incorrect id format for row {i}"

def test_task_func_category_values():
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    df = task_func(5, categories=categories)
    for row in df.iterrows():
        assert row['category'] in categories, "Category should be one of the specified categories"

def test_task_func_views_distribution():
    df = task_func(1000, random_seed=42)
    views = df['views'].values
    assert np.all(views >= 0), "Views should be non-negative"
    assert np.mean(views) > 900 and np.mean(views) < 1100, "Mean views should be around 1000"

def test_task_func_random_seed_consistency():
    df1 = task_func(5, random_seed=42)
    df2 = task_func(5, random_seed=42)
    assert df1.equals(df2), "DataFrames should be identical with the same random seed"