python
import os
import pandas as pd
import pytest

def task_func(filename: str) -> pd.DataFrame:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No such file: '{filename}'")

    if os.stat(filename).st_size == 0:
        # File is empty, return an empty DataFrame with no columns.
        return pd.DataFrame()

    df = pd.read_csv(filename)

    # Erase the original file's content using a context manager to handle the file properly
    with open(filename, 'w') as file:
        file.truncate()

    return df

def test_task_func():
    # Test case 1: File does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv')

    # Test case 2: File is empty
    df = task_func('empty_file.csv')
    assert df.empty

    # Test case 3: File is not empty
    with open('test_file.csv', 'w') as file:
        file.write('col1,col2\n1,2\n3,4')
    df = task_func('test_file.csv')
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ['col1', 'col2']
    assert df.iloc[0, 0] == 1
    assert df.iloc[1, 1] == 4
    os.remove('test_file.csv')