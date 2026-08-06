import pytest
from src_0180 import task_func
import pandas as pd

@pytest.fixture
def sample_dataframe():
    data = {
        'Title': ['How to learn Python', 'What is data science', 'Introduction to Machine Learning'],
        'Content': ['Learn Python now', 'Data science is important', 'Machine learning techniques']
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    result = task_func(sample_dataframe)
    assert result is not None

def test_no_interesting_articles(sample_dataframe):
    data = sample_dataframe.copy()
    data['Title'] = ['What is Python', 'Introduction to Data Science']
    result = task_func(data)
    assert result is None

def test_no_columns(sample_dataframe):
    data = sample_dataframe.drop(columns=['Title', 'Content'])
    result = task_func(data)
    assert result is None

def test_no_interesting_articles(sample_dataframe):
    data = sample_dataframe.copy()
    data['Title'] = ['What is Python', 'Introduction to Data Science']
    result = task_func(data)
    assert result is None