import pytest
from src_0779 import task_func

def test_task_func():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Article 1', 'title_url': 'article1.com'},
        {'category': 'sports', 'id': 2, 'title': 'Article 2', 'title_url': 'article2.com'},
        {'category': 'politics', 'id': 3, 'title': 'Article 3', 'title_url': 'article3.com'},
        {'category': 'politics', 'id': 4, 'title': 'Article 4', 'title_url': 'article4.com'},
        {'category': 'sports', 'id': 5, 'title': 'Article 5', 'title_url': 'article5.com'},
    ]
    expected_result = {
        'sports': [
            {'category': 'sports', 'id': 1, 'title': 'Article 1', 'title_url': 'article1.com'},
            {'category': 'sports', 'id': 2, 'title': 'Article 2', 'title_url': 'article2.com'},
            {'category': 'sports', 'id': 5, 'title': 'Article 5', 'title_url': 'article5.com'},
        ],
        'politics': [
            {'category': 'politics', 'id': 3, 'title': 'Article 3', 'title_url': 'article3.com'},
            {'category': 'politics', 'id': 4, 'title': 'Article 4', 'title_url': 'article4.com'},
        ],
    }
    assert task_func(news_articles) == expected_result

def test_task_func_invalid_input():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Article 1', 'title_url': 'article1.com'},
        {'category': 'sports', 'id': 2, 'title': 'Article 2', 'title_url': 'article2.com'},
        {'category': 'politics', 'id': 3, 'title': 'Article 3', 'title_url': 'article3.com'},
        {'category': 'politics', 'id': 4, 'title': 'Article 4', 'title_url': 'article4.com'},
        {'category': 'sports', 'id': 5, 'title': 'Article 5', 'title_url': 'article5.com'},
    ]
    news_articles[0]['category'] = 'invalid'
    with pytest.raises(ValueError):
        task_func(news_articles)