import pandas as pd
import os
import pytest

from src_0889 import task_func

@pytest.fixture
def csv_files():
    return ['file1.csv', 'file2.csv', 'file3.csv']

@pytest.fixture
def data_dir(tmp_path):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()
    for file in csv_files():
        data_dir.joinpath(file).write_text('dummy data')
    return str(data_dir)

def test_task_func(data_dir, csv_files):
    merged_df = task_func(data_dir, csv_files)
    assert isinstance(merged_df, pd.DataFrame)
    assert len(merged_df) == len(csv_files)