import os

import pandas as pd
import pytest
from dateutil.parser import parse
from src_0647 import task_func

OUTPUT_DIR = './output'

def test_task_func_file_not_found():
    csv_path = os.path.join(OUTPUT_DIR, 'nonexistent.csv')
    with pytest.raises(FileNotFoundError):
        task_func(csv_path)

def test_task_func_valid_csv():
    csv_path = os.path.join(OUTPUT_DIR, 'data.csv')
    df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03']})
    df['date'] = df['date'].apply(lambda x: parse(x))
    expected_hist = df['date'].dt.year.value_counts()
    actual_hist = task_func(csv_path)
    assert actual_hist.equals(expected_hist)