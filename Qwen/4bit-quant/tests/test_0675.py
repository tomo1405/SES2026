import pytest
from src_0675 import task_func
import os
import pandas as pd

def test_task_func_file_not_exists():
    filename = "non_existent_file.csv"
    result = task_func(filename)
    assert result == filename

def test_task_func_empty_file():
    filename = "empty_file.csv"
    with open(filename, 'w') as file:
        pass
    result = task_func(filename)
    assert result == filename
    os.remove(filename)

def test_task_func_non_empty_file():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
    filename = "non_empty_file.csv"
    df.to_csv(filename, index=False)

    result = task_func(filename)
    assert result == filename

    reversed_df = pd.read_csv(filename)
    assert reversed_df.equals(df.iloc[::-1])

    os.remove(filename)