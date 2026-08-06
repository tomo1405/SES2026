import pytest
from src_0779 import task_func

def test_task_func():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
        {'category': 'sports', 'id': 2, 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'},
        {'category': 'politics', 'id': 3, 'title': 'Article 3', 'title_url': 'https://www.example.com/article3'},
        {'category': 'politics', 'id': 4, 'title': 'Article 4', 'title_url': 'https://www.example.com/article4'},
        {'category': 'entertainment', 'id': 5, 'title': 'Article 5', 'title_url': 'https://www.example.com/article5'},
        {'category': 'entertainment', 'id': 6, 'title': 'Article 6', 'title_url': 'https://www.example.com/article6'}
    ]

    grouped_articles = task_func(news_articles)

    assert grouped_articles == {
        'sports': [
            {'category': 'sports', 'id': 1, 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
            {'category': 'sports', 'id': 2, 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'}
        ],
        'politics': [
            {'category': 'politics', 'id': 3, 'title': 'Article 3', 'title_url': 'https://www.example.com/article3'},
            {'category': 'politics', 'id': 4, 'title': 'Article 4', 'title_url': 'https://www.example.com/article4'}
        ],
        'entertainment': [
            {'category': 'entertainment', 'id': 5, 'title': 'Article 5', 'title_url': 'https://www.example.com/article5'},
            {'category': 'entertainment', 'id': 6, 'title': 'Article 6', 'title_url': 'https://www.example.com/article6'}
        ]
    }