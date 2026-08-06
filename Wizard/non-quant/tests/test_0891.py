python
import os
import random
import pandas as pd
import pytest

def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):

    random.seed(seed)

    file = csv_files[random.randint(0, len(csv_files) - 1)]
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return file, pd.DataFrame()

    selected_rows = df.sample(n=random.randint(1, len(df)), random_state=seed)

    return file, selected_rows

def test_task_func():
    data_dir = 'data'
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
    seed = 42

    file, selected_rows = task_func(data_dir, csv_files, seed)

    assert file in csv_files
    assert isinstance(selected_rows, pd.DataFrame)
    assert len(selected_rows) <= len(pd.read_csv(os.path.join(data_dir, file)))