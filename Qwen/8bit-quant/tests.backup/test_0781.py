import pytest
from src_0781 import task_func
import pandas as pd
import pytz

def test_task_func_invalid_articles_type():
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func("not a list", "UTC")

def test_task_func_invalid_article_type():
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func([{}, "not a dict"], "UTC")

def test_task_func_empty_articles_list():
    with pytest.raises(ValueError, match="input articles list should contain at least one article."):
        task_func([], "UTC")

def test_task_func_missing_keys():
    with pytest.raises(ValueError, match="input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'"):
        task_func([{"missing_key": "value"}], "UTC")

def test_task_func_valid_input():
    articles = [
        {
            "category": "news",
            "id": 1,
            "title": "Title 1",
            "title_url": "url1",
            "published_time": "2023-10-01T12:00:00Z"
        },
        {
            "category": "news",
            "id": 2,
            "title": "Title 2",
            "title_url": "url2",
            "published_time": "2023-10-01T14:00:00Z"
        }
    ]
    expected_output = pd.DataFrame({
        'count': [2],
        'mean': [13.0],
        'min': [12],
        'max': [14]
    }, index=['news'])
    result = task_func(articles, "UTC")
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_different_timezone():
    articles = [
        {
            "category": "news",
            "id": 1,
            "title": "Title 1",
            "title_url": "url1",
            "published_time": "2023-10-01T12:00:00Z"
        },
        {
            "category": "news",
            "id": 2,
            "title": "Title 2",
            "title_url": "url2",
            "published_time": "2023-10-01T14:00:00Z"
        }
    ]
    expected_output = pd.DataFrame({
        'count': [2],
        'mean': [9.0],
        'min': [8],
        'max': [10]
    }, index=['news'])
    result = task_func(articles, "America/New_York")
    pd.testing.assert_frame_equal(result, expected_output)