python
import pandas as pd
import time
import pytest

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(data, letter):
    df = pd.DataFrame(data)
    start_time = time.time()
    regex = f'^{letter}'
    filtered_df = df[df['Name'].str.contains(regex, case=False, regex=True)]
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return filtered_df['Name'].value_counts()

def test_task_func():
    data = {'Name': ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Mike', 'Mary', 'Peter', 'David'],
            'Age': [25, 30, 40, 20, 35, 45, 28, 32, 42]}
    letter = 'a'
    expected_result = pd.Series([2, 1], index=['Alice', 'David'])
    result = task_func(data, letter)
    assert result.equals(expected_result)