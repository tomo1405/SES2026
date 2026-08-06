import pytest
from src_0061 import task_func
import pandas as pd
import json

def test_task_func():
    # Test data
    result = {'key1': 'value1', 'key2': 'value2'}
    expected_csv_content = 'key1,key2\nvalue1,value2\n'
    expected_json_content = '{\n    "key1": "value1",\n    "key2": "value2"\n}'

    # Call the function
    task_func(result)

    # Check CSV file
    with open('test.csv', 'r') as f:
        assert f.read() == expected_csv_content

    # Check JSON file
    with open('test.json', 'r') as f:
        assert f.read() == expected_json_content

    # Clean up
    import os
    os.remove('test.csv')
    os.remove('test.json')