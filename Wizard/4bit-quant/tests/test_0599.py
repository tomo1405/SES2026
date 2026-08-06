python
import pandas as pd
import time
import pytest

def task_func(df, letter):
    start_time = time.time()
    df = pd.DataFrame(df)
    regex = '^' + letter
    filtered_df = df[df['Word'].str.contains(regex, regex=True)]
    word_lengths = filtered_df['Word'].str.len()
    count_dict = word_lengths.value_counts().to_dict()
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."

    return count_dict

def test_task_func():
    # Test case 1
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']}
    letter = 'b'
    expected_result = {3: 1, 6: 1}
    assert task_func(df, letter) == expected_result

    # Test case 2
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']}
    letter = 'd'
    expected_result = {4: 1}
    assert task_func(df, letter) == expected_result

    # Test case 3
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']}
    letter = 'z'
    expected_result = {}
    assert task_func(df, letter) == expected_result