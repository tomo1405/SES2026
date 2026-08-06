import pytest
from src_0779 import task_func

def test_task_func_valid_input():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Football', 'title_url': 'https://www.sportsnews.com/football'},
        {'category': 'sports', 'id': 2, 'title': 'Tennis', 'title_url': 'https://www.sportsnews.com/tennis'},
        {'category': 'technology', 'id': 1, 'title': 'Tech Giants', 'title_url': 'https://www.technews.com/tech-giants'},
        {'category': 'technology', 'id': 2, 'title': 'AI', 'title_url': 'https://www.technews.com/ai'},
    ]
    expected_output = {
        'sports': [
            {'category': 'sports', 'id': 1, 'title': 'Football', 'title_url': 'https://www.sportsnews.com/football'},
            {'category': 'sports', 'id': 2, 'title': 'Tennis', 'title_url': 'https://www.sportsnews.com/tennis'},
        ],
        'technology': [
            {'category': 'technology', 'id': 1, 'title': 'Tech Giants', 'title_url': 'https://www.technews.com/tech-giants'},
            {'category': 'technology', 'id': 2, 'title': 'AI', 'title_url': 'https://www.technews.com/ai'},
        ],
    }
    assert task_func(news_articles) == expected_output

def test_task_func_invalid_input():
    news_articles = [
        {'category': 'sports', 'id': 1, 'title': 'Football', 'title_url': 'https://www.sportsnews.com/football'},
        {'category': 'sports', 'id': 2, 'title': 'Tennis', 'title_url': 'https://www.sportsnews.com/tennis'},
        {'category': 'technology', 'id': 1, 'title': 'Tech Giants', 'title_url': 'https://www.technews.com/tech-giants'},
        {'category': 'technology', 'id': 2, 'title': 'AI', 'title_url': 'https://www.technews.com/ai'},
    ]
    news_articles[0]['category'] = 'invalid'
    with pytest.raises(ValueError) as exc_info:
        task_func(news_articles)
    assert str(exc_info.value) == "input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url'"