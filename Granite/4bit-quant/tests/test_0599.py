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
    df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
    letter = 'b'
    expected_output = {5: 2}
    actual_output = task_func(df, letter)
    assert actual_output == expected_output, "Output does not match expected output"

test_task_func()