import json
import numpy as np
import pandas as pd
import pytest

from src_0708 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({'IntCol': [1, 10, 100, 1000]})

def test_task_func(input_df):
    output_df = task_func(input_df)
    assert 'IntCol' in output_df.columns
    assert output_df['IntCol'].tolist() == [0, 1, 2, 3]
    assert len(output_df) == 4

def test_json_output(input_df, tmpdir):
    output_df = task_func(input_df)
    int_col_list = output_df['IntCol'].tolist()
    expected_json = json.dumps(int_col_list)

    json_file_path = tmpdir.join('IntCol.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(int_col_list, json_file)

    with open(json_file_path) as json_file:
        actual_json = json_file.read()

    assert actual_json == expected_json