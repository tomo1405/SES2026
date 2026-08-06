import pytest
from src_0178 import task_func
import pandas as pd
import nltk

# Download necessary NLTK data files
nltk.download('punkt')

@pytest.fixture
def sample_df():
    data = {
        'Title': ['What is Python?', 'Introduction to Programming', 'Like Python?'],
        'Content': [
            'Python is a great programming language.',
            'Programming can be fun.',
            'I like Python very much.'
        ]
    }
    return pd.DataFrame(data)

def test_task_func_missing_columns():
    df = pd.DataFrame({'Title': ['Test']})
    with pytest.raises(ValueError, match="DataFrame must include 'Title' and 'Content' columns."):
        task_func(df)

def test_task_func_no_interesting_articles(sample_df):
    df = sample_df[sample_df['Title'] != 'What is Python?']
    result = task_func(df)
    assert result == {}

def test_task_func_with_interesting_articles(sample_df):
    result = task_func(sample_df)
    expected = {
        'Python': 3,
        'is': 1,
        'a': 1,
        'great': 1,
        'programming': 2,
        'language': 1,
        'Introduction': 1,
        'to': 1,
        'can': 1,
        'be': 1,
        'fun': 1,
        'I': 1,
        'like': 1,
        'very': 1,
        'much': 1
    }
    assert result == expected

def test_task_func_empty_content(sample_df):
    df = sample_df.copy()
    df.loc[0, 'Content'] = ''
    result = task_func(df)
    expected = {
        'Python': 2,
        'is': 1,
        'a': 1,
        'great': 1,
        'programming': 1,
        'language': 1,
        'Introduction': 1,
        'to': 1,
        'can': 1,
        'be': 1,
        'fun': 1,
        'I': 1,
        'like': 1,
        'very': 1,
        'much': 1
    }
    assert result == expected