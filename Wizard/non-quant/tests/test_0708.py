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
    # Test case 1: Test with a dataframe with integer column
    df = pd.DataFrame({'IntCol': [1, 2, 3, 4, 5]})
    expected_df = pd.DataFrame({'IntCol': [0.0, 0.30103, 0.47712, 0.60206, 0.69897]})
    expected_json = '["0.0", "0.30103", "0.47712", "0.60206", "0.69897"]'

    # Call the function and get the result
    result_df = task_func(df)

    # Check if the result matches the expected result
    assert_frame_equal(result_df, expected_df)

    # Check if the JSON file contains the expected data
    with open('IntCol.json', 'r') as json_file:
        result_json = json_file.read()

    assert result_json == expected_json

    # Test case 2: Test with a dataframe with float column
    df = pd.DataFrame({'FloatCol': [1.0, 2.0, 3.0, 4.0, 5.0]})
    expected_df = pd.DataFrame({'FloatCol': [0.0, 0.30103, 0.47712, 0.60206, 0.69897]})
    expected_json = '["0.0", "0.30103", "0.47712", "0.60206", "0.69897"]'

    # Call the function and get the result
    result_df = task_func(df)

    # Check if the result matches the expected result
    assert_frame_equal(result_df, expected_df)

    # Check if the JSON file contains the expected data
    with open('IntCol.json', 'r') as json_file:
        result_json = json_file.read()

    assert result_json == expected_json