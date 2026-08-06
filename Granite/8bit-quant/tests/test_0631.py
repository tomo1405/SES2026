import json
import os

import pandas as pd
from src_0631 import task_func


def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, 5, 6]})
    
    # Call the function with the sample DataFrame and a filename
    filename = 'output.json'
    file_path = task_func(df, filename)
    
    # Assert that the returned file path is as expected
    expected_file_path = os.path.join(OUTPUT_DIR, filename)
    assert file_path == expected_file_path
    
    # Assert that the output file exists
    assert os.path.exists(file_path)
    
    # Assert that the contents of the output file are as expected
    with open(file_path, 'r') as f:
        data = json.load(f)
    expected_data = df.where(pd.notnull(df), None).to_dict(orient='records')
    assert data == expected_data