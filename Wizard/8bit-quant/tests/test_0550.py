python
import base64
import pandas as pd
import pytest

def task_func(df):
    df = pd.DataFrame(df)
    csv = df.to_csv(index=False)
    csv_bytes = csv.encode('utf-8')
    base64_bytes = base64.b64encode(csv_bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string

def test_task_func():
    # Test case 1: Test with a valid input
    input_df = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    expected_output = 'U2VuZCBhIHNob3VsZCBiZSBhZGRyZXNzIHlvdXIgZGVmYXVsdA==\n'
    assert task_func(input_df) == expected_output

    # Test case 2: Test with an empty input
    input_df = []
    expected_output = ''
    assert task_func(input_df) == expected_output

    # Test case 3: Test with a None input
    input_df = None
    expected_output = ''
    assert task_func(input_df) == expected_output

    # Test case 4: Test with a non-list input
    input_df = 'not a list'
    expected_output = ''
    assert task_func(input_df) == expected_output