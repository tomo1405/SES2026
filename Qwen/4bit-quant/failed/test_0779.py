import pytest
from src_0779 import task_func

def test_task_func_valid_input():
    articles = [
        {'category': 'Sports', 'id': 1, 'title': 'Football Match', 'title_url': 'url1'},
        {'category': 'Sports', 'id': 2, 'title': 'Basketball Game', 'title_url': 'url2'},
        {'category': 'Tech', 'id': 3, 'title': 'New Phone Release', 'title_url': 'url3'},
        {'category': 'Tech', 'id': 4, 'title': 'AI Update', 'title_url': 'url4'}
    ]
    expected_output = {
        'Sports': [
            {'category': 'Sports', 'id': 1, 'title': 'Football Match', 'title_url': 'url1'},
            {'category': 'Sports', 'id': 2, 'title': 'Basketball Game', 'title_url': 'url2'}
        ],
        'Tech': [
            {'category': 'Tech', 'id': 3, 'title': 'New Phone Release', 'title_url': 'url3'},
            {'category': 'Tech', 'id': 4, 'title': 'AI Update', 'title_url': 'url4'}
        ]
    }
    assert task_func(articles) == expected_output

def test_task_func_missing_key():
    articles = [
        {'category': 'Sports', 'id': 1, 'title': 'Football Match', 'title_url': 'url1'},
        {'category': 'Sports', 'id': 2, 'title': 'Basketball Game'}  # Missing 'title_url'
    ]
    with pytest.raises(ValueError, match="input dictionaries must contain the following keys: 'category', 'id', 'title', 'title_url'"):
        task_func(articles)

def test_task_func_extra_key():
    articles = [
        {'category': 'Sports', 'id': 1, 'title': 'Football Match', 'title_url': 'url1', 'extra': 'value'},
        {'category': 'Sports', 'id': 2, 'title': 'Basketball Game', 'title_url': 'url2'}
    ]
    expected_output = {
        'Sports': [
            {'category': 'Sports', 'id': 1, 'title': 'Football Match', 'title_url': 'url1', 'extra': 'value'},
            {'category': 'Sports', 'id': 2, 'title': 'Basketball Game', 'title_url': 'url2'}
        ]
    }
    assert task_func(articles) == expected_output

def test_task_func_empty_input():
    articles = []
    expected_output = {}
    assert task_func(articles) == expected_output

def test_task_func_single_article():
    articles = [
        {'category': 'Tech', 'id': 1, 'title': 'New Phone Release', 'title_url': 'url1'}
    ]
    expected_output = {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'New Phone Release', 'title_url': 'url1'}
        ]
    }
    assert task_func(articles) == expected_output