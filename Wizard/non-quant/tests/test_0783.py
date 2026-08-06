python
import random
import pandas as pd
import numpy as np
import pytest

def task_func(n, domain="samplewebsite.com", categories=['Sports', 'Technology', 'Health', 'Science', 'Business'], random_seed=None):
    random.seed(random_seed)
    np.random.seed(random_seed)

    data = []
    for _ in range(n):
        title = f"Article {_}"
        title_url = f"{domain}/Article_{_}"
        id = _
        category = random.choice(categories)
        views = np.random.poisson(1000)
        data.append({'title': title, 'title_url': title_url, 'id': id, 'category': category, 'views': views})

    df = pd.DataFrame(data)
    return df

def test_task_func():
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.columns.tolist() == ['title', 'title_url', 'id', 'category', 'views']
    assert df['title'][0] == 'Article 0'
    assert df['title_url'][0] == 'samplewebsite.com/Article_0'
    assert df['id'][0] == 0
    assert df['category'][0] in ['Sports', 'Technology', 'Health', 'Science', 'Business']
    assert df['views'][0] >= 0

def test_task_func_random_seed():
    df1 = task_func(10, random_seed=123)
    df2 = task_func(10, random_seed=123)
    assert df1.equals(df2)

def test_task_func_categories():
    df = task_func(10, categories=['Sports', 'Technology'])
    assert df['category'].isin(['Sports', 'Technology']).all()

def test_task_func_domain():
    df = task_func(10, domain='example.com')
    assert df['title_url'].str.startswith('example.com/Article_').all()

def test_task_func_n():
    df = task_func(10)
    assert df.shape == (10, 5)
    df = task_func(0)
    assert df.shape == (0, 5)
    df = task_func(1)
    assert df.shape == (1, 5)
    df = task_func(1000)
    assert df.shape == (1000, 5)