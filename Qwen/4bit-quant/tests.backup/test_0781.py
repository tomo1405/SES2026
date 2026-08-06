import pytest
from src_0781 import task_func
import pandas as pd
import pytz

def test_task_func_with_valid_input():
    articles = [
        {
            'category': 'news',
            'id': 1,
            'published_time': '2023-10-01T12:00:00Z',
            'title': 'Test Title 1',
            'title_url': 'http://example.com/1'
        },
        {
            'category': 'news',
            'id': 2,
            'published_time': '2023-10-01T14:00:00Z',
            'title': 'Test Title 2',
            'title_url': 'http://example.com/2'
        }
    ]
    timezone = 'America/New_York'
    result = task_func(articles, timezone)
    expected_columns = ['count', 'mean', 'min', 'max']
    assert all(col in result.columns for col in expected_columns)
    assert 'news' in result.index
    assert result.loc['news', 'count'] == 2

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([], 'UTC')

def test_task_func_with_non_list_input():
    with pytest.raises(TypeError):
        task_func({}, 'UTC')

def test_task_func_with_non_dict_items():
    with pytest.raises(TypeError):
        task_func([{}, []], 'UTC')

def test_task_func_with_missing_keys():
    articles = [
        {
            'category': 'news',
            'id': 1,
            'published_time': '2023-10-01T12:00:00Z',
            'title': 'Test Title 1',
        }
    ]
    with pytest.raises(ValueError):
        task_func(articles, 'UTC')

def test_task_func_with_invalid_timezone():
    articles = [
        {
            'category': 'news',
            'id': 1,
            'published_time': '2023-10-01T12:00:00Z',
            'title': 'Test Title 1',
            'title_url': 'http://example.com/1'
        }
    ]
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(articles, 'Invalid/Timezone')