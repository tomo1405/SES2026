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
    data = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}, {'Name': 'Charlie', 'Age': 35}]
    letter = 'B'
    expected_output = {'Bob': 1}
    actual_output = task_func(data, letter)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()