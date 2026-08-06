import pytest
from src_0783 import task_func

def test_task_func():
    n = 10
    domain = "samplewebsite.com"
    categories = ['Sports', 'Technology', 'Health', 'Science', 'Business']
    random_seed = 42

    df = task_func(n, domain, categories, random_seed)

    assert len(df) == n
    assert all(df['title'].str.startswith('Article'))
    assert all(df['title_url'].str.startswith(f'{domain}/Article_'))
    assert all(df['id'].astype(int) == np.arange(n))
    assert all(df['category'].isin(categories))
    assert all(df['views'].astype(int) >= 0)