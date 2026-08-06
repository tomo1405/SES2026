import os
import time
import pytest
from src_0630 import task_func

OUTPUT_DIR = './output'

def test_task_func():
    dataset = [pd.DataFrame({'a': range(10)}), pd.DataFrame({'b': range(5)})]
    filename = 'test_file.csv'
    task_func(dataset, filename)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    assert '------' in content
    assert 'index' not in content
    assert content.count('\n') == len(dataset) - 1