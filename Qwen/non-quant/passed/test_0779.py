import pytest
from src_0779 import task_func
from collections import defaultdict

def test_task_func_valid_input():
    input_data = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'url1'},
        {'category': 'Tech', 'id': 2, 'title': 'Machine Learning', 'title_url': 'url2'},
        {'category': 'Science', 'id': 3, 'title': 'Space Exploration', 'title_url': 'url3'}
    ]
    expected_output = defaultdict(list, {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'url1'},
            {'category': 'Tech', 'id': 2, 'title': 'Machine Learning', 'title_url': 'url2'}
        ],
        'Science': [
            {'category': 'Science', 'id': 3, 'title': 'Space Exploration', 'title_url': 'url3'}
        ]
    })
    assert task_func(input_data) == expected_output

def test_task_func_invalid_keys():
    input_data = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances'},
        {'category': 'Tech', 'id': 2, 'title': 'Machine Learning', 'title_url': 'url2'}
    ]
    with pytest.raises(ValueError):
        task_func(input_data)

def test_task_func_empty_input():
    input_data = []
    expected_output = defaultdict(list)
    assert task_func(input_data) == expected_output

def test_task_func_single_category():
    input_data = [
        {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'url1'},
        {'category': 'Tech', 'id': 2, 'title': 'Machine Learning', 'title_url': 'url2'}
    ]
    expected_output = defaultdict(list, {
        'Tech': [
            {'category': 'Tech', 'id': 1, 'title': 'AI Advances', 'title_url': 'url1'},
            {'category': 'Tech', 'id': 2, 'title': 'Machine Learning', 'title_url': 'url2'}
        ]
    })
    assert task_func(input_data) == expected_output

def test_task_func_multiple_categories_unsorted_titles():
    input_data = [
        {'category': 'Tech', 'id': 1, 'title': 'Z AI Advances', 'title_url': 'url1'},
        {'category': 'Tech', 'id': 2, 'title': 'A Machine Learning', 'title_url': 'url2'},
        {'category': 'Science', 'id': 3, 'title': 'C Space Exploration', 'title_url': 'url3'},
        {'category': 'Science', 'id': 4, 'title': 'B Astronomy', 'title_url': 'url4'}
    ]
    expected_output = defaultdict(list, {
        'Tech': [
            {'category': 'Tech', 'id': 2, 'title': 'A Machine Learning', 'title_url': 'url2'},
            {'category': 'Tech', 'id': 1, 'title': 'Z AI Advances', 'title_url': 'url1'}
        ],
        'Science': [
            {'category': 'Science', 'id': 4, 'title': 'B Astronomy', 'title_url': 'url4'},
            {'category': 'Science', 'id': 3, 'title': 'C Space Exploration', 'title_url': 'url3'}
        ]
    })
    assert task_func(input_data) == expected_output