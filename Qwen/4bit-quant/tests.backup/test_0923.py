import pytest
from src_0923 import task_func

def test_task_func_with_empty_data():
    data = []
    column = 'text'
    result_df = task_func(data, column)
    assert result_df.empty, "Expected an empty DataFrame"

def test_task_func_with_single_row():
    data = [{'text': 'This is a test sentence.'}]
    column = 'text'
    expected_output = {'text': ['test sentence']}
    result_df = task_func(data, column)
    assert result_df.to_dict(orient='records') == expected_output, "Expected output does not match"

def test_task_func_with_multiple_rows():
    data = [
        {'text': 'This is a test sentence.'},
        {'text': 'Another example with more words.'}
    ]
    column = 'text'
    expected_output = {
        'text': ['test sentence', 'example with more words']
    }
    result_df = task_func(data, column)
    assert result_df.to_dict(orient='records') == expected_output, "Expected output does not match"

def test_task_func_with_stopwords_only():
    data = [{'text': 'is a test of stopwords'}]
    column = 'text'
    expected_output = {'text': ['test stopwords']}
    result_df = task_func(data, column)
    assert result_df.to_dict(orient='records') == expected_output, "Expected output does not match"

def test_task_func_with_punctuation():
    data = [{'text': 'Hello, world! How are you today?'}]
    column = 'text'
    expected_output = {'text': ['Hello world How are you today']}
    result_df = task_func(data, column)
    assert result_df.to_dict(orient='records') == expected_output, "Expected output does not match"

def test_task_func_with_numbers():
    data = [{'text': 'The price is 100 dollars.'}]
    column = 'text'
    expected_output = {'text': ['price dollars']}
    result_df = task_func(data, column)
    assert result_df.to_dict(orient='records') == expected_output, "Expected output does not match"