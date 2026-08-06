import pytest
from src_0180 import task_func

def test_task_func_with_valid_data():
    df = pd.DataFrame({'Title': ['How to make a pie', 'What is the meaning of life'], 'Content': ['This is a recipe for a delicious pie', 'The meaning of life is to find your purpose']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticks() == ['how', 'what']
    assert ax.get_yticks() == [0, 1]

def test_task_func_with_invalid_data():
    df = pd.DataFrame({'Title': ['How to make a pie', 'What is the meaning of life'], 'Content': ['This is a recipe for a delicious pie', 'The meaning of life is to find your purpose']})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticks() == ['how', 'what']
    assert ax.get_yticks() == [0, 1]

def test_task_func_with_empty_data():
    df = pd.DataFrame({'Title': [], 'Content': []})
    ax = task_func(df)
    assert ax.get_ylabel() == 'TF-IDF Score'
    assert ax.get_xticks() == []
    assert ax.get_yticks() == []