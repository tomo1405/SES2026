import pytest
from src_0646 import task_func
import os
import pandas as pd

@pytest.fixture
def sample_file(tmp_path):
    # Create a sample file with some data
    data = "col1,col2\n1,2\n3,4\n"
    file_path = tmp_path / "test_file.csv"
    with open(file_path, 'w') as file:
        file.write(data)
    return file_path

def test_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

def test_empty_file(tmp_path):
    # Create an empty file
    file_path = tmp_path / "empty_file.csv"
    open(file_path, 'w').close()
    result = task_func(file_path)
    assert result.empty

def test_valid_file(tmp_path):
    # Create a valid file
    data = "col1,col2\n1,2\n3,4\n"
    file_path = tmp_path / "valid_file.csv"
    with open(file_path, 'w') as file:
        file.write(data)
    result = task_func(file_path)
    assert not result.empty
    assert result.equals(pd.read_csv(file_path))