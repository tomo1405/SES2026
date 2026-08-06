import json
import os

import numpy as np
import pandas as pd
import pytest
from src_0708 import task_func


@pytest.fixture
def sample_df():
    data = {'IntCol': [10, 100, 1000]}
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df = task_func(sample_df)
    
    # Check if 'IntCol' has been transformed correctly
    expected_int_col = np.log10([10, 100, 1000])
    assert np.allclose(result_df['IntCol'], expected_int_col), "The 'IntCol' values were not transformed correctly."
    
    # Check if the JSON file was created and contains the correct data
    assert os.path.exists('IntCol.json'), "The JSON file was not created."
    
    with open('IntCol.json', 'r') as json_file:
        json_data = json.load(json_file)
    
    assert np.allclose(json_data, expected_int_col), "The JSON file does not contain the correct data."

    # Clean up the JSON file after the test
    os.remove('IntCol.json')