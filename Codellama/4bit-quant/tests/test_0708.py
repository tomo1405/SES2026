import json

import numpy as np
import pandas as pd
from src_0708 import task_func


def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'IntCol': [1, 10, 100, 1000]})

    # Test that the function modifies the DataFrame correctly
    df_modified = task_func(df)
    assert np.allclose(df_modified['IntCol'], np.log10(df['IntCol']))

    # Test that the function writes the correct data to the JSON file
    with open('IntCol.json', 'r') as json_file:
        int_col_list = json.load(json_file)
    assert int_col_list == df['IntCol'].tolist()