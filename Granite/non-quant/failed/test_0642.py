import os
import re
import pandas as pd
import pytest
from src_0642 import task_func

def test_task_func():
    # Test case 1: pattern matches one file
    pattern = r'example\.txt'
    directory = '/path/to/directory'
    output_csv = '/path/to/output.csv'
    expected_df = pd.DataFrame({'File Path': ['/path/to/directory/example.txt']})

    with pytest.warns(UserWarning, match='No files matched the pattern'):
        actual_df = task_func(pattern, directory, output_csv)

    assert actual_df.equals(expected_df)

    # Test case 2: pattern matches multiple files
    pattern = r'.*\.txt'
    directory = '/path/to/directory'
    output_csv = '/path/to/output.csv'
    expected_df = pd.DataFrame({'File Path': ['/path/to/directory/file1.txt', '/path/to/directory/file2.txt']})

    with pytest.warns(None) as record:
        actual_df = task_func(pattern, directory, output_csv)

    assert actual_df.equals(expected_df)
    assert len(record) == 1
    assert record[0].message.args[0] == '2 files matched the pattern'