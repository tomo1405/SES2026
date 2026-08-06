python
import pandas as pd
import os
import pytest

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df_clean = df.where(pd.notnull(df), None)
    with open(file_path, 'w') as f:
        df_clean.to_json(f, orient='records')
    return file_path

def test_task_func():
    # Test case 1: normal case
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    filename = 'test.json'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    os.remove(file_path)

    # Test case 2: empty dataframe
    df = pd.DataFrame()
    filename = 'test.json'
    file_path = task_func(df, filename)
    assert os.path.exists(file_path)
    os.remove(file_path)

    # Test case 3: non-existent output directory
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    filename = 'test.json'
    output_dir = 'nonexistent_dir'
    file_path = task_func(df, filename, output_dir=output_dir)
    assert os.path.exists(file_path)
    os.remove(file_path)