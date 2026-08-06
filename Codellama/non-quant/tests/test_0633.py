import json
import os
import time

import pandas as pd
from src_0633 import task_func


def test_task_func():
    # Test case 1: Test that the function returns the correct file path
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    filename = 'test_file.json'
    expected_file_path = os.path.join(OUTPUT_DIR, filename)
    assert task_func(df, filename) == expected_file_path

    # Test case 2: Test that the function creates the correct file
    assert os.path.exists(expected_file_path)
    with open(expected_file_path, 'r') as file:
        data = json.load(file)
        assert data == df.to_dict(orient='records')

    # Test case 3: Test that the function returns the correct cost
    start_time = time.time()
    task_func(df, filename)
    end_time = time.time()
    expected_cost = f"Operation completed in {end_time - start_time} seconds."
    assert task_func(df, filename) == expected_cost