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
            'title': 'Tennis',
            'title_url': 'https://www.sportsnews.com/tennis',
            'published_time': '2022-01-02 13:00:00'
        }
    ]
    timezone = 'US/Eastern'
    result = task_func(articles, timezone)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 5)
    assert list(result.columns) == ['count', 'mean', 'min', 'max', 'published_time']

def test_task_func_invalid_input():
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
            'title': 'Tennis',
            'title_url': 'https://www.sportsnews.com/tennis',
            'published_time': '2022-01-02 13:00:00'
        },
        {
            'category': 'sports',
            'id': '3',
            'title': 'Basketball',
            'title_url': 'https://www.sportsnews.com/basketball',
            'published_time': '2022-01-03 14:00:00'
        }
    ]
    timezone = 'US/Eastern'
    with pytest.raises(ValueError) as excinfo:
        task_func(articles, timezone)
    assert str(excinfo.value) == "input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'"