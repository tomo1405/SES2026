python
import random
import pandas as pd
import numpy as np
import pytest

def task_func(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
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
    # Test case 1: n=10, random_seed=42
    df = task_func(10, random_seed=42)
    assert df.shape == (10, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['views'] == 1011
    assert df.iloc[9]['title'] == 'Article 9'
    assert df.iloc[9]['views'] == 1003

    # Test case 2: n=5, random_seed=None
    df = task_func(5)
    assert df.shape == (5, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['views'] == 1009
    assert df.iloc[4]['title'] == 'Article 4'
    assert df.iloc[4]['views'] == 1002

    # Test case 3: n=1, random_seed=123
    df = task_func(1, random_seed=123)
    assert df.shape == (1, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['views'] == 1006

    # Test case 4: n=0, random_seed=None
    df = task_func(0)
    assert df.shape == (0, 5)

    # Test case 5: n=1000, random_seed=None
    df = task_func(1000)
    assert df.shape == (1000, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['views'] == 1009
    assert df.iloc[999]['title'] == 'Article 999'
    assert df.iloc[999]['views'] == 1002