import pytest
from src_0633 import task_func
import pandas as pd
import time
import os
import json

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    filename = 'test_data.jsonl'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    with open(file_path, 'r') as file:
        records = [json.loads(line) for line in file]
        assert records == [{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}]
    os.remove(file_path)