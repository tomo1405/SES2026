import pytest
from src_0682 import task_func
import pandas as pd
import json

def test_task_func():
    file_path = 'test_data.json'
    key = 'key'
    data = {'key': 'value'}
    with open(file_path, 'w') as file:
        json.dump(data, file)

    df = task_func(file_path, key)

    assert df.shape[0] == 1
    assert df.shape[1] == 0

    with open(file_path, 'r') as file:
        data = json.load(file)

    assert data == []