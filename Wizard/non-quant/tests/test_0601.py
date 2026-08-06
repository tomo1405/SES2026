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
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon'],
          'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    letter = 'b'
    expected_result = {'mean': 4.0, 'median': 4.0, 'mode': 6}
    result = task_func(df, letter)
    assert result == expected_result

test_task_func()