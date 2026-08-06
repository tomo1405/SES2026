import pytest
from src_0779 import task_func

def test_task_func():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Team A wins', 'title_url': 'www.news.com/article1'},
        {'category': 'sports', 'id': 2, 'title': 'Team B wins', 'title_url': 'www.news.com/article2'},
        {'category': 'science', 'id': 3, 'title': 'New discovery', 'title_url': 'www.news.com/article3'},
        {'category': 'science', 'id': 4, 'title': 'New theory', 'title_url': 'www.news.com/article4'},
    ]
    expected_output = {
        'sports': [
            {'category': 'sports', 'id': 1, 'title': 'Team A wins', 'title_url': 'www.news.com/article1'},
            {'category': 'sports', 'id': 2, 'title': 'Team B wins', 'title_url': 'www.news.com/article2'},
        ],
        'science': [
            {'category': 'science', 'id': 3, 'title': 'New discovery', 'title_url': 'www.news.com/article3'},
            {'category': 'science', 'id': 4, 'title': 'New theory', 'title_url': 'www.news.com/article4'},
        ],
    }
    assert task_func(news_articles) == expected_output

def test_task_func_with_invalid_input():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Team A wins', 'title_url': 'www.news.com/article1'},
        {'category': 'sports', 'id': 2, 'title': 'Team B wins', 'title_url': 'www.news.com/article2'},
        {'category': 'science', 'id': 3, 'title': 'New discovery', 'title_url': 'www.news.com/article3'},
        {'category': 'science', 'id': 4, 'title': 'New theory', 'title_url': 'www.news.com/article4'},
        {'category': 'sports', 'id': 5, 'title_url': 'www.news.com/article5'},
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(news_articles)
    assert str(exc_info.value) == "input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url'"