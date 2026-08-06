import pandas as pd
import pytest
from src_0646 import task_func


def test_task_func_valid_file():
    filename = 'test_data.csv'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.to_csv(filename, index=False)

    result = task_func(filename)

    assert result.equals(df)

def test_task_func_invalid_file():
    filename = 'invalid_file.csv'

    with pytest.raises(FileNotFoundError):
        task_func(filename)

def test_task_func_empty_file():
    filename = 'empty_file.csv'
    with open(filename, 'w') as file:
        file.truncate()

    result = task_func(filename)

    assert result.empty

def test_task_func_invalid_file_type():
    filename = 'invalid_file_type.txt'

    with pytest.raises(ValueError):
        task_func(filename)