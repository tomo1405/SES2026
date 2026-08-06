import pytest
from src_0781 import task_func

def test_task_func():
    articles = [
        {'category': 'sports', 'id': 1, 'published_time': '2022-01-01 12:00:00', 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
        {'category': 'sports', 'id': 2, 'published_time': '2022-01-01 13:00:00', 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'},
        {'category': 'sports', 'id': 3, 'published_time': '2022-01-01 14:00:00', 'title': 'Article 3', 'title_url': 'https://www.example.com/article3'},
        {'category': 'sports', 'id': 4, 'published_time': '2022-01-01 15:00:00', 'title': 'Article 4', 'title_url': 'https://www.example.com/article4'},
        {'category': 'sports', 'id': 5, 'published_time': '2022-01-01 16:00:00', 'title': 'Article 5', 'title_url': 'https://www.example.com/article5'},
    ]
    timezone = 'America/New_York'
    expected_result = pd.DataFrame({
        'category': ['sports'],
        'count': [5],
        'mean': [13.0],
        'min': [12.0],
        'max': [16.0]
    })

    result = task_func(articles, timezone)

    assert result.equals(expected_result)