python
import os
import re
import pandas as pd
import pytest

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    matched_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_paths.append(os.path.join(root, file))

    df = pd.DataFrame(matched_paths, columns=['File Path'])
    df.to_csv(output_csv, index=False)

    return df

def test_task_func():
    # Test case 1: pattern is valid regex, directory exists, output_csv is a valid path
    pattern = r'\.txt$'
    directory = 'tests/test_files'
    output_csv = 'tests/test_output.csv'
    expected_df = pd.DataFrame({'File Path': ['tests/test_files/test1.txt', 'tests/test_files/test2.txt']})
    actual_df = task_func(pattern, directory, output_csv)
    assert actual_df.equals(expected_df)

    # Test case 2: pattern is invalid regex, directory does not exist, output_csv is a valid path
    pattern = r'\.csv$'
    directory = 'tests/test_files_not_exist'
    output_csv = 'tests/test_output.csv'
    with pytest.raises(FileNotFoundError):
        task_func(pattern, directory, output_csv)

    # Test case 3: pattern is valid regex, directory exists, output_csv is a valid path, but directory is empty
    pattern = r'\.txt$'
    directory = 'tests/test_files_empty'
    output_csv = 'tests/test_output.csv'
    expected_df = pd.DataFrame({'File Path': []})
    actual_df = task_func(pattern, directory, output_csv)
    assert actual_df.equals(expected_df)