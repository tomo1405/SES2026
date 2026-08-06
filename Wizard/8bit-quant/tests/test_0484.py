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
    # Test case 1: No pattern provided
    df = pd.DataFrame({'text': ['hello world', 'goodbye world']})
    new_df = task_func(df, 'text', '')
    assert new_df.equals(df)

    # Test case 2: Pattern provided
    df = pd.DataFrame({'text': ['hello world', 'goodbye world']})
    new_df = task_func(df, 'text', 'world')
    expected_df = pd.DataFrame({'text': ['olleh dlrow', 'dgoobye dlrow']})
    assert new_df.equals(expected_df)

    # Test case 3: Pattern provided with multiple matches
    df = pd.DataFrame({'text': ['hello world', 'goodbye world', 'hello python']})
    new_df = task_func(df, 'text', 'world')
    expected_df = pd.DataFrame({'text': ['olleh dlrow', 'dgoobye dlrow', 'olleh nohtyp']})
    assert new_df.equals(expected_df)

    # Test case 4: Pattern provided with no matches
    df = pd.DataFrame({'text': ['hello world', 'goodbye world']})
    new_df = task_func(df, 'text', 'java')
    expected_df = pd.DataFrame({'text': ['hello world', 'goodbye world']})
    assert new_df.equals(expected_df)