import pytest
from src_0183 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'Title': ['How to learn Python', 'What is machine learning', 'Introduction to AI', 'Python basics'],
        'Content': ['Python is a great language', 'Machine learning is fascinating', 'AI changes the world', 'Basics of Python']
    }
    return pd.DataFrame(data)

def test_task_func_no_interesting_articles(sample_df):
    # Modify the title to not match the pattern
    sample_df['Title'] = ['Introduction to Python', 'Basics of Machine Learning', 'AI Overview', 'Python Fundamentals']
    result = task_func(sample_df)
    assert result == []

def test_task_func_with_interesting_articles(sample_df):
    result = task_func(sample_df)
    assert isinstance(result, list)
    assert len(result) == 2  # There are 2 articles that match the pattern

def test_task_func_single_interesting_article():
    data = {
        'Title': ['How to learn Python'],
        'Content': ['Python is a great language']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, list)
    assert len(result) == 1

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    result = task_func(df)
    assert result == []

def test_task_func_all_articles_interesting():
    data = {
        'Title': ['How to learn Python', 'What is machine learning'],
        'Content': ['Python is a great language', 'Machine learning is fascinating']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, list)
    assert len(result) == 2