python
import re
import pandas as pd
import pytest

def task_func(input_df):
    def clean_text_and_calculate_length(row):
        if pd.isnull(row['text']):
            return pd.Series(['', 0], index=['clean_text', 'text_length'])
        cleaned_text = re.sub('[^A-Za-z0-9]+', '', str(row['text']))
        return pd.Series([cleaned_text, len(cleaned_text)], index=['clean_text', 'text_length'])
    
    return input_df.apply(clean_text_and_calculate_length, axis=1)

def test_task_func():
    input_df = pd.DataFrame({'text': ['Hello, World!', '12345', None]})
    expected_output = pd.DataFrame({'clean_text': ['HelloWorld', '12345', ''], 'text_length': [10, 5, 0]})
    assert task_func(input_df).equals(expected_output)

if __name__ == '__main__':
    test_task_func()