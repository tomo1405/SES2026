import pytest
from src_0183 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'Title': ['How to learn Python', 'What is machine learning?', 'Introduction to AI', 'Python basics'],
        'Content': ['Python is a versatile language.', 'Machine learning is a subset of AI.', 'AI has many applications.', 'Basics of Python programming.']
    }
    return pd.DataFrame(data)

def test_task_func_no_interesting_articles(sample_df):
    # Modify the DataFrame to have no titles matching the pattern
    sample_df['Title'] = ['General topic', 'Another general topic']
    result = task_func(sample_df)
    assert result == []

def test_task_func_with_interesting_articles(sample_df):
    result = task_func(sample_df)
    assert isinstance(result, list)
    assert len(result) == 2  # Only two articles match the pattern

def test_task_func_kmeans_labels(sample_df):
    result = task_func(sample_df)
    assert all(isinstance(label, int) for label in result)
    assert set(result) == {0, 1}  # Assuming two clusters are formed

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Title', 'Content'])
    result = task_func(df)
    assert result == []