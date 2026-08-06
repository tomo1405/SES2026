import os
import random
import pandas as pd
import pytest

from src_0891 import task_func

@pytest.mark.parametrize("data_dir,csv_files,seed", [
    ("/path/to/data", ["file1.csv", "file2.csv", "file3.csv"], 42),
    ("/another/path/to/data", ["file4.csv", "file5.csv"], 13),
])
def test_task_func(data_dir, csv_files, seed):
    file, selected_rows = task_func(data_dir, csv_files, seed)

    assert file in csv_files
    assert isinstance(selected_rows, pd.DataFrame)
    assert len(selected_rows) > 0