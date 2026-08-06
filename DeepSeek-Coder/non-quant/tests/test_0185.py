import pytest
from src_0185 import task_func
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re

# Define a sample dataframe for testing
data = {
    'text_column': [
        "This is a sample text. It has some words and numbers 123.",
        "Another text with more words and 456.",
    ]
}
df = pd.DataFrame(data)

def test_task_func():
    result = task_func(df, 'text_column')
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The result DataFrame should not be empty"
    assert set(result.columns) == {'this', 'is', 'a', 'sample', 'text', 'it', 'has', 'some', 'words', 'and', 'numbers', 'another', 'text', 'with', 'more', 'words', 'and', 'numbers'}