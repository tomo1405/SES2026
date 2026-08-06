import pytest
from src_0783 import task_func

def test_task_func():
    n = 10
    domain = "samplewebsite.com"
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    random_seed = 42

    df = task_func(n, domain, categories, random_seed)

    assert len(df) == n
    assert df['title'].dtype == object
    assert df['title_url'].dtype == object
    assert df['id'].dtype == int
    assert df['category'].dtype == object
    assert df['views'].dtype == int

    for i in range(n):
        assert df.iloc[i]['title'] == f"Article {i}"
        assert df.iloc[i]['title_url'] == f"{domain}/Article_{i}"
        assert df.iloc[i]['id'] == i
        assert df.iloc[i]['category'] in categories
        assert df.iloc[i]['views'] >= 0