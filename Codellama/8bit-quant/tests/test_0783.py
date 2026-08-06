import pytest
from src_0783 import task_func

def test_task_func():
    n = 10
    domain = "samplewebsite.com"
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    random_seed = 42

    df = task_func(n, domain, categories, random_seed)

    assert len(df) == n
    assert df['title'].str.contains('Article').all()
    assert df['title_url'].str.contains(domain).all()
    assert df['id'].astype(int).all()
    assert df['category'].isin(categories).all()
    assert df['views'].astype(int).all()