import pytest
from src_0923 import task_func
import pandas as pd
import re

# Define test data
test_data = {
    'text': [
        "This is a test sentence. This sentence is for testing.",
        "Another sentence with some words."
    ]
}

def test_task_func():
    result = task_func(test_data, 'text')
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == len(test_data['text']), "The result should have the same number of rows as the input data"
    assert 'text' in result.columns, "The result should have the 'text' column"
    assert all(isinstance(word, str) for row in result['text'] for word in row.split()), "Each word should be a string"
    assert all(word.lower() not in STOPWORDS for row in result['text'] for word in row.split()), "All words should be free of stopwords"