import pytest
from src_0781 import task_func

def test_task_func_type_error():
    articles = [{'category': 'sports', 'id': 1, 'published_time': '2022-01-01 12:00:00', 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
                {'category': 'sports', 'id': 2, 'published_time': '2022-01-01 13:00:00', 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'}]
    timezone = 'America/New_York'
    with pytest.raises(TypeError):
        task_func(articles, timezone)

def test_task_func_value_error():
    articles = [{'category': 'sports', 'id': 1, 'published_time': '2022-01-01 12:00:00', 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
                {'category': 'sports', 'id': 2, 'published_time': '2022-01-01 13:00:00', 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'}]
    timezone = 'America/New_York'
    with pytest.raises(ValueError):
        task_func(articles, timezone)

def test_task_func_success():
    articles = [{'category': 'sports', 'id': 1, 'published_time': '2022-01-01 12:00:00', 'title': 'Article 1', 'title_url': 'https://www.example.com/article1'},
                {'category': 'sports', 'id': 2, 'published_time': '2022-01-01 13:00:00', 'title': 'Article 2', 'title_url': 'https://www.example.com/article2'}]
    timezone = 'America/New_York'
    result = task_func(articles, timezone)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1, 4)
    assert result.columns.tolist() == ['category', 'count', 'mean', 'min']
    assert result.loc['sports', 'count'] == 2
    assert result.loc['sports', 'mean'] == 13
    assert result.loc['sports', 'min'] == 12
    assert result.loc['sports', 'max'] == 13