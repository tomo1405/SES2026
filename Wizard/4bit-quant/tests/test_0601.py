python
import pandas as pd
import numpy as np
import pytest

def task_func(df, letter):
    df = pd.DataFrame(df)
    regex = '^' + letter
    filtered_df = df[df['Word'].str.contains(regex, regex=True)]
    word_lengths = filtered_df['Word'].str.len()
    statistics = {'mean': np.mean(word_lengths), 'median': np.median(word_lengths), 'mode': word_lengths.mode().values[0]}

    return statistics

def test_task_func():
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon'], 'Count': [10, 5, 15, 20, 12, 8, 18, 14, 6, 11]}
    letter = 'b'
    expected_result = {'mean': 5.0, 'median': 5.0, 'mode': 5}
    result = task_func(df, letter)
    assert result == expected_result