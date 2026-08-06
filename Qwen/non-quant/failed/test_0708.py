import pytest
from src_0708 import task_func
import pandas as pd
import numpy as np
import os

def test_task_func():
    # Create a sample DataFrame
    data = {'IntCol': [10, 100, 1000]}
    df = pd.DataFrame(data)
    
    # Expected output DataFrame after applying log10
    expected_data = {'IntCol': [1.0, 2.0, 3.0]}
    expected_df = pd.DataFrame(expected_data)
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the DataFrame is modified correctly
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check if the JSON file is created and contains the correct data
    assert os.path.exists('IntCol.json')
    with open('IntCol.json', 'r') as json_file:
        json_data = json.load(json_file)
    assert json_data == [1.0, 2.0, 3.0]
    
    # Clean up the JSON file
    os.remove('IntCol.json')