import pytest
from src_0779 import task_func

def test_task_func_valid_input():
    news_articles = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'},
        {'category': 'Science', 'id': 2, 'title': 'Space Exploration', 'title_url': 'space-exploration'},
        {'category': 'Tech', 'id': 3, 'title': 'Quantum Computing', 'title_url': 'quantum-computing'}
    ]
    expected_output = {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'},
            {'category': 'Tech', 'id': 3, 'title': 'Quantum Computing', 'title_url': 'quantum-computing'}
        ],
        'Science': [
            {'category': 'Science', 'id': 2, 'title': 'Space Exploration', 'title_url': 'space-exploration'}
        ]
    }
    assert task_func(news_articles) == expected_output

def test_task_func_missing_key():
    news_articles = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances'},
        {'category': 'Science', 'id': 2, 'title': 'Space Exploration', 'title_url': 'space-exploration'}
    ]
    with pytest.raises(ValueError):
        task_func(news_articles)

def test_task_func_empty_list():
    news_articles = []
    expected_output = {}
    assert task_func(news_articles) == expected_output

def test_task_func_single_article():
    news_articles = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'}
    ]
    expected_output = {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'}
        ]
    }
    assert task_func(news_articles) == expected_output

def test_task_func_same_category_different_titles():
    news_articles = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'},
        {'category': 'Tech', 'id': 2, 'title': 'Quantum Computing', 'title_url': 'quantum-computing'}
    ]
    expected_output = {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'ai-advances'},
            {'category': 'Tech', 'id': 2, 'title': 'Quantum Computing', 'title_url': 'quantum-computing'}
        ]
    }
    assert task_func(news_articles) == expected_output