python
import re
import pandas as pd
import pytest

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:

    def reverse_matched_words(text):
        words = text.split()
        matched_words = [word for word in words if re.search(pattern, word)][::-1]
        new_words = [
            matched_words.pop(0) if re.search(pattern, word) else word for word in words
        ]
        return " ".join(new_words)

    new_df = df.copy()
    if not pattern:
        return new_df
    new_df[column_name] = new_df[column_name].apply(reverse_matched_words)
    return new_df

def test_task_func():
    df = pd.DataFrame({'text': ['The quick brown fox jumps over the lazy dog', 'The dog is not amused']})
    column_name = 'text'
    pattern = 'not'
    expected_df = pd.DataFrame({'text': ['The quick brown fox jumps over the lazy dog', 'The dog is amused']})
    result_df = task_func(df, column_name, pattern)
    assert result_df.equals(expected_df)