python
import pandas as pd
import time

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

# Test the function
def test_task_func():
    data = [
        {'Name': 'Alice', 'Age': 25},
        {'Name': 'Bob', 'Age': 30},
        {'Name': 'Charlie', 'Age': 35},
        {'Name': 'Dave', 'Age': 40},
        {'Name': 'Eve', 'Age': 45},
        {'Name': 'Frank', 'Age': 50},
        {'Name': 'Grace', 'Age': 55},
        {'Name': 'Henry', 'Age': 60},
        {'Name': 'Isaac', 'Age': 65},
        {'Name': 'Jack', 'Age': 70},
    ]
    letter = 'a'
    expected_result = pd.Series({'Alice': 1})
    result = task_func(data, letter)
    assert result.equals(expected_result)

test_task_func()