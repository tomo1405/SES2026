import json
import numpy as np
import pandas as pd
import pytest
from src_0708 import task_func

def test_task_func():
    # Create a sample DataFrame with an 'IntCol' column
    df = pd.DataFrame({'IntCol': [1, 10, 100, 1000]})

    # Call the function and store the returned DataFrame
    result_df = task_func(df)

    # Check if the 'IntCol' column has been converted to a list
    assert isinstance(result_df['IntCol'], list)

    # Check if the list has the correct length
    assert len(result_df['IntCol']) == 4

    # Check if the list contains the correct values
    assert result_df['IntCol'] == [0.0, 1.0, 2.0, 3.0]

    # Check if a JSON file has been created
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)

    # Check if the JSON file contains the correct data
    assert int_col_list == [0.0, 1.0, 2.0, 3.0]