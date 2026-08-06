import os
import json
import pandas as pd
import time
import pytest

from src_0633 import task_func

OUTPUT_DIR = './output'

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})

    # Call the function with the sample DataFrame and a filename
    file_path = task_func(df, 'test_file.json')

    # Assert that the file path returned by the function exists
    assert os.path.exists(file_path)

    # Assert that the file contains valid JSON lines
    with open(file_path, 'r') as file:
        for line in file:
            assert json.loads(line) in df.to_dict(orient='records')

    # Assert that the operation completed within a reasonable time
    start_time = time.time()
    file_path = task_func(df, 'test_file.json')
    end_time = time.time()
    assert end_time - start_time < 1  # Adjust the threshold as needed

if __name__ == '__main__':
    pytest.main()