import json

import numpy as np
import pandas as pd
from src_0708 import task_func


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'IntCol': [1, 10, 100, 1000]})

    # Test that the function returns the expected dataframe
    expected_df = pd.DataFrame({'IntCol': [1, 10, 100, 1000]})
    expected_df['IntCol'] = np.log10(expected_df['IntCol'])
    assert task_func(df).equals(expected_df)

    # Test that the function writes the expected JSON file
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)
    assert int_col_list == [1, 10, 100, 1000]