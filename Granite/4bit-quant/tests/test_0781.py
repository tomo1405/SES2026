import pandas as pd
import pytest
from src_0781 import task_func


def test_task_func_valid_input():
    articles = [
        {
            'category': 'sports',
            'id': '1',
            'title': 'Football',
            'title_url': 'https://www.sportsnews.com/football',
            'published_time': '2022-01-01 12:00:00'
        },
        {
            'category': 'sports',
            'id': '2',
            'title': 'Basketball',
            'title_url': 'https://www.sportsnews.com/basketball',
            'published_time': '2022-01-02 13:00:00'
        }
    ]
    timezone = 'America/New_York'
    expected_output = pd.DataFrame({
        'published_time': {
            'count': [2],
            'mean': [14.5],
            'min': [12.0],
            'max': [15.0]
        }
    }, index=pd.Index(['sports'], name='category'))
    actual_output = task_func(articles, timezone)
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_task_func_invalid_input():
    articles = 'not a list'
    timezone = 'America/New_York'
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func(articles, timezone)

    articles = [
        {
            'category': 'sports',
            'id': '1',
            'title': 'Football',
            'title_url': 'https://www.sportsnews.com/football',
            'published_time': '2022-01-01 12:00:00'
        },
        'not a dict'
    ]
    timezone = 'America/New_York'
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func(articles, timezone)

    articles = []
    timezone = 'America/New_York'
    with pytest.raises(ValueError, match="input articles list should contain at least one article."):
        task_func(articles, timezone)

    articles = [
        {
            'category': 'sports',
            'id': '1',
            'title': 'Football',
            'title_url': 'https://www.sportsnews.com/football',
            'published_time': '2022-01-01 12:00:00'
        },
        {
            'category': 'sports',
            'id': '2',
            'title': 'Basketball',
            'title_url': 'https://www.sportsnews.com/basketball'
        }
    ]
    timezone = 'America/New_York'
    with pytest.raises(ValueError, match="input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'"):
        task_func(articles, timezone)