import pytest
from src_0781 import task_func
import pandas as pd
import pytz

def test_task_func_invalid_articles_type():
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func("not a list", "UTC")

def test_task_func_invalid_articles_content():
    with pytest.raises(TypeError, match="articles should be a list of dictionaries."):
        task_func([{}, "not a dict"], "UTC")

def test_task_func_empty_articles():
    with pytest.raises(ValueError, match="input articles list should contain at least one article."):
        task_func([], "UTC")

def test_task_func_missing_keys():
    with pytest.raises(ValueError, match="input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url', 'published_time'"):
        task_func([{"id": 1, "title": "Test", "title_url": "http://example.com"}], "UTC")

def test_task_func_valid_input():
    articles = [
        {"category": "news", "id": 1, "title": "Test 1", "title_url": "http://example.com/1", "published_time": "2023-10-01T12:00:00Z"},
        {"category": "news", "id": 2, "title": "Test 2", "title_url": "http://example.com/2", "published_time": "2023-10-01T14:00:00Z"},
        {"category": "sports", "id": 3, "title": "Test 3", "title_url": "http://example.com/3", "published_time": "2023-10-01T09:00:00Z"}
    ]
    result = task_func(articles, "America/New_York")
    expected_columns = ['count', 'mean', 'min', 'max']
    assert all(col in result.columns for col in expected_columns)
    assert len(result) == 2  # Two categories: news and sports
    assert result.loc['news', 'count'] == 2
    assert result.loc['sports', 'count'] == 1

def test_task_func_timezone_conversion():
    articles = [
        {"category": "news", "id": 1, "title": "Test 1", "title_url": "http://example.com/1", "published_time": "2023-10-01T12:00:00Z"},
    ]
    result = task_func(articles, "America/New_York")
    assert result.loc['news', 'mean'] == 8  # 12:00 UTC is 8:00 AM EST

def test_task_func_empty_category():
    articles = [
        {"category": "", "id": 1, "title": "Test 1", "title_url": "http://example.com/1", "published_time": "2023-10-01T12:00:00Z"},
    ]
    result = task_func(articles, "UTC")
    assert result.loc['', 'count'] == 1