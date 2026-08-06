python
import os
import json
import pandas as pd
import time
import pytest

OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    start_time = time.time()
    # Ensure the data directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    file_path = os.path.join(OUTPUT_DIR, filename)

    # Save DataFrame as JSON Lines
    with open(file_path, 'w') as file:
        for record in df.to_dict(orient='records'):
            json.dump(record, file)
            file.write('\n')
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return os.path.abspath(file_path)

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.jsonl'
    expected_output = os.path.join(OUTPUT_DIR, filename)
    assert task_func(df, filename) == expected_output

    # Test case 2: Test with invalid input (empty DataFrame)
    df = pd.DataFrame()
    filename = 'test.jsonl'
    with pytest.raises(ValueError):
        task_func(df, filename)

    # Test case 3: Test with invalid input (filename with invalid extension)
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test.txt'
    with pytest.raises(ValueError):
        task_func(df, filename)