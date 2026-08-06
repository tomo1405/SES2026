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
    # Test case 1: Valid input
    pattern = r'\.txt$'
    directory = 'tests/test_files'
    output_csv = 'tests/test_output.csv'
    expected_df = pd.DataFrame({'File Path': ['tests/test_files/test1.txt', 'tests/test_files/test2.txt']})
    actual_df = task_func(pattern, directory, output_csv)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input (empty directory)
    pattern = r'\.txt$'
    directory = 'tests/empty_directory'
    output_csv = 'tests/test_output.csv'
    with pytest.raises(ValueError):
        task_func(pattern, directory, output_csv)

    # Test case 3: Invalid input (non-existent directory)
    pattern = r'\.txt$'
    directory = 'tests/nonexistent_directory'
    output_csv = 'tests/test_output.csv'
    with pytest.raises(FileNotFoundError):
        task_func(pattern, directory, output_csv)

    # Test case 4: Invalid input (invalid pattern)
    pattern = r'\.tx$'
    directory = 'tests/test_files'
    output_csv = 'tests/test_output.csv'
    with pytest.raises(re.error):
        task_func(pattern, directory, output_csv)

    # Test case 5: Invalid input (invalid output file)
    pattern = r'\.txt$'
    directory = 'tests/test_files'
    output_csv = 'tests/nonexistent_directory/test_output.csv'
    with pytest.raises(FileNotFoundError):
        task_func(pattern, directory, output_csv)