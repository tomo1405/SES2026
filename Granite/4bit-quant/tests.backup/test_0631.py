import pandas as pd
import os
import pytest

from src_0631 import task_func

OUTPUT_DIR = './output'

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    filename = 'test_file.json'
    file_path = task_func(df, filename)
    assert file_path == os.path.join(OUTPUT_DIR, filename)
    assert os.path.exists(file_path)
    with open(file_path) as f:
        data = json.load(f)
    assert data == [{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}]