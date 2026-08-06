python
import json
import numpy as np
import pytest

def task_func(df):
    df['IntCol'] = np.log10(df['IntCol'])

    # Convert 'IntCol' column to a list and write it to a JSON file
    int_col_list = df['IntCol'].tolist()
    with open('IntCol.json', 'w') as json_file:
        json.dump(int_col_list, json_file)

    return df

def test_task_func():
    # Test case 1: Test with a valid dataframe
    df = pd.DataFrame({'IntCol': [1, 10, 100]})
    expected_df = pd.DataFrame({'IntCol': [0, 1, 2]})
    expected_json = '["0.0", "1.0", "2.0"]'
    task_func(df)
    with open('IntCol.json', 'r') as json_file:
        actual_json = json_file.read()
    assert expected_df.equals(df)
    assert expected_json == actual_json

    # Test case 2: Test with an empty dataframe
    df = pd.DataFrame({'IntCol': []})
    expected_df = pd.DataFrame({'IntCol': []})
    expected_json = '[]'
    task_func(df)
    with open('IntCol.json', 'r') as json_file:
        actual_json = json_file.read()
    assert expected_df.equals(df)
    assert expected_json == actual_json

    # Test case 3: Test with a dataframe with negative values
    df = pd.DataFrame({'IntCol': [-1, -10, -100]})
    expected_df = pd.DataFrame({'IntCol': [-0.0, -1.0, -2.0]})
    expected_json = '["-0.0", "-1.0", "-2.0"]'
    task_func(df)
    with open('IntCol.json', 'r') as json_file:
        actual_json = json_file.read()
    assert expected_df.equals(df)
    assert expected_json == actual_json

    # Test case 4: Test with a dataframe with NaN values
    df = pd.DataFrame({'IntCol': [1, np.nan, 100]})
    expected_df = pd.DataFrame({'IntCol': [0.0, np.nan, 2.0]})
    expected_json = '["0.0", "null", "2.0"]'
    task_func(df)
    with open('IntCol.json', 'r') as json_file:
        actual_json = json_file.read()
    assert expected_df.equals(df)
    assert expected_json == actual_json

    # Test case 5: Test with a dataframe with all NaN values
    df = pd.DataFrame({'IntCol': [np.nan, np.nan, np.nan]})
    expected_df = pd.DataFrame({'IntCol': [np.nan, np.nan, np.nan]})
    expected_json = '["null", "null", "null"]'
    task_func(df)
    with open('IntCol.json', 'r') as json_file:
        actual_json = json_file.read()
    assert expected_df.equals(df)
    assert expected_json == actual_json