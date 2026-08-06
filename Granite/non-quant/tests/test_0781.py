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
            'published_time': '2022-01-01 13:00:00'
        }
    ]
    timezone = 'US/Eastern'
    analysis_df = task_func(articles, timezone)
    assert isinstance(analysis_df, pd.DataFrame)
    assert analysis_df.shape == (2, 5)
    assert analysis_df.columns.tolist() == ['count', 'mean', 'min', 'max', 'published_time']

def test_task_func_invalid_input():
    articles = 'not a list'
    timezone = 'US/Eastern'
    with pytest.raises(TypeError) as exc_info:
        task_func(articles, timezone)
    assert str(exc_info.value) == "articles should be a list of dictionaries."

def test_task_func_empty_list():
    articles = []
    timezone = 'US/Eastern'
    with pytest.raises(ValueError) as exc_info:
        task_func(articles, timezone)
    assert str(exc_info.value) == "input articles list should contain at least one article."

def test_task_func_missing_key():
    articles = [
        {
            'category': 'sports',
            'id': '1',
            'title': 'Football',
            'title_url': 'https://www.sportsnews.com/football'
        }
    ]
    timezone = 'US/Eastern'
    with pytest.raises(ValueError) as exc_info:
        task_func(articles, timezone)
    assert str(exc_info.value) == "input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'"