import pandas as pd
from texttable import Texttable
import os
import glob
import pytest

def task_func(data_dir='./data/'):
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The directory '{data_dir}' does not exist.")

    data_files = sorted(glob.glob(os.path.join(data_dir, '*.csv')))
    if not data_files:
        raise ValueError(f"No CSV files found in the directory '{data_dir}'.")

    summary_data = []
    for file in data_files:
        try:
            data = pd.read_csv(file)
            summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])
        except pd.errors.EmptyDataError:
            # Handle empty CSV file
            raise pd.errors.EmptyDataError(f"Error when reading file '{file}'.")
        data = pd.read_csv(file)
        summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])

    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)

    return table.draw()

def test_task_func():
    with pytest.raises(FileNotFoundError):
        task_func(data_dir='./non-existent-directory')

    with pytest.raises(ValueError):
        task_func(data_dir='./data')

    with pytest.raises(pd.errors.EmptyDataError):
        task_func(data_dir='./data/empty_csv_files')

    assert isinstance(task_func(), str)