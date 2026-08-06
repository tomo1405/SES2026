import pytest
from src_0891 import task_func

def test_task_func():
    data_dir = 'path/to/data/dir'
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
    seed = 1234

    file, selected_rows = task_func(data_dir, csv_files, seed)

    assert file in csv_files
    assert isinstance(selected_rows, pd.DataFrame)
    assert len(selected_rows) > 0
    assert selected_rows.index.name == 'index'
    assert selected_rows.columns.name == 'column'