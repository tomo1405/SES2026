python
import re
import pandas as pd
import pytest

def clean_text_and_calculate_length(row):
    if pd.isnull(row['text']):
        return pd.Series(['', 0], index=['clean_text', 'text_length'])
    cleaned_text = re.sub('[^A-Za-z0-9]+', '', str(row['text']))
    return pd.Series([cleaned_text, len(cleaned_text)], index=['clean_text', 'text_length'])

def test_task_func():
    input_df = pd.DataFrame({'text': ['This is a test', '12345', None]})
    expected_output = pd.DataFrame({'clean_text': ['Thisisatest', '12345', ''], 'text_length': [11, 5, 0]})
    output = task_func(input_df)
    assert output.equals(expected_output)