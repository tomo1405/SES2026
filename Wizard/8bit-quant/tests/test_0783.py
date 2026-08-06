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
    # Test case 1
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['title_url'] == 'samplewebsite.com/Article_0'
    assert df.iloc[0]['id'] == 0
    assert df.iloc[0]['category'] in ['Sports', 'Technology', 'Health', 'Science', 'Business']
    assert df.iloc[0]['views'] >= 0

    # Test case 2
    df = task_func(5, random_seed=42)
    assert df.shape == (5, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['title_url'] == 'samplewebsite.com/Article_0'
    assert df.iloc[0]['id'] == 0
    assert df.iloc[0]['category'] in ['Sports', 'Technology', 'Health', 'Science', 'Business']
    assert df.iloc[0]['views'] >= 0

    # Test case 3
    df = task_func(10, domain="mywebsite.com", categories=['Sports', 'Technology', 'Health'], random_seed=123)
    assert df.shape == (10, 5)
    assert df.iloc[0]['title'] == 'Article 0'
    assert df.iloc[0]['title_url'] == 'mywebsite.com/Article_0'
    assert df.iloc[0]['id'] == 0
    assert df.iloc[0]['category'] in ['Sports', 'Technology', 'Health']
    assert df.iloc[0]['views'] >= 0

    # Test case 4
    with pytest.raises(ValueError):
        task_func(-1)

    # Test case 5
    with pytest.raises(ValueError):
        task_func(10, categories=['Sports', 'Technology', 'Health', 'Science', 'Business', 'Entertainment'])

    # Test case 6
    with pytest.raises(ValueError):
        task_func(10, random_seed='abc')