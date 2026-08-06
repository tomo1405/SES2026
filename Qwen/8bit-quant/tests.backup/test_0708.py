import pytest
from src_0708 import task_func
import pandas as pd
import os
import json

def test_task_func():
    # Create a sample DataFrame
    data = {'IntCol': [10, 100, 1000]}
    df = pd.DataFrame(data)
    
    # Expected output after applying the function
    expected_df = df.copy()
    expected_df['IntCol'] = np.log10(expected_df['IntCol'])
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the DataFrame is modified correctly
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check if the JSON file is created and contains the correct data
    assert os.path.exists('IntCol.json')
    with open('IntCol.json', 'r') as json_file:
        json_data = json.load(json_file)
    expected_json_data = expected_df['IntCol'].tolist()
    assert json_data == expected_json_data
    
    # Clean up the JSON file
    os.remove('IntCol.json')