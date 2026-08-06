python
import re
import os
import glob
import natsort
import pandas as pd
import pytest

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    files = natsort.natsorted(glob.glob(os.path.join(directory, file_pattern)))
    if not files:
        raise ValueError(f"No files found matching pattern '{file_pattern}' in directory '{directory}'.")

    data = []
    for filename in files:
        with open(filename, 'r') as file:
            content = file.read()
        numeric_data = re.findall(regex, content)
        data.append([os.path.basename(filename), numeric_data])

    df = pd.DataFrame(data, columns=['Filename', 'Numeric Data'])

    return df

def test_task_func():
    # Test case 1: Valid directory, file pattern, and regex
    df = task_func(directory='./tests/test_files', file_pattern='*.txt', regex=r'([0-9]+)')
    assert df.shape == (2, 2)
    assert df.loc[0, 'Filename'] == 'file1.txt'
    assert df.loc[0, 'Numeric Data'] == ['1', '2', '3']
    assert df.loc[1, 'Filename'] == 'file2.txt'
    assert df.loc[1, 'Numeric Data'] == ['4', '5', '6']

    # Test case 2: Invalid directory
    with pytest.raises(FileNotFoundError):
        task_func(directory='./tests/invalid_directory', file_pattern='*.txt', regex=r'([0-9]+)')

    # Test case 3: No files found
    with pytest.raises(ValueError):
        task_func(directory='./tests/test_files', file_pattern='*.csv', regex=r'([0-9]+)')

    # Test case 4: Invalid regex pattern
    with pytest.raises(re.error):
        task_func(directory='./tests/test_files', file_pattern='*.txt', regex=r'([a-z]+)')