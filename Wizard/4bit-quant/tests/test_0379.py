python
import pandas as pd
from texttable import Texttable
import os
import glob

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir')

    # Test case 2: Directory exists but no CSV files
    with pytest.raises(ValueError):
        task_func('data/empty_dir')

    # Test case 3: Directory exists with CSV files
    summary_data = [
        ['file1.csv', 3, 4],
        ['file2.csv', 5, 6],
        ['file3.csv', 7, 8],
    ]
    expected_table = Texttable()
    expected_table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    assert task_func('data/') == expected_table.draw()

    # Test case 4: Directory exists with CSV files and empty CSV file
    summary_data = [
        ['file1.csv', 3, 4],
        ['file2.csv', 5, 6],
        ['file3.csv', 7, 8],
        ['empty.csv', 0, 0],
    ]
    expected_table = Texttable()
    expected_table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    assert task_func('data/empty_csv') == expected_table.draw()