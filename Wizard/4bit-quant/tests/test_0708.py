python
import json
import numpy as np
import pandas as pd
import pytest

from src_0708 import task_func

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'IntCol': [1, 10, 100]})

    # Call the task function
    result = task_func(df)

    # Check if the output file exists
    assert os.path.exists('IntCol.json')

    # Read the output file and check if it matches the expected output
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)
        assert int_col_list == [0.0, 1.0, 2.0]

    # Check if the original dataframe is unchanged
    assert df.equals(pd.DataFrame({'IntCol': [1, 10, 100]}))