import pytest
from src_0646 import task_func
import pandas as pd
import os

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="No such file: 'non_existent_file.csv'"):
        task_func('non_existent_file.csv')

def test_task_func_empty_file(tmp_path):
    empty_file = tmp_path / "empty_file.csv"
    empty_file.touch()

    result_df = task_func(str(empty_file))
    assert result_df.empty
    assert result_df.shape == (0, 0)

def test_task_func_non_empty_file(tmp_path):
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    file_path = tmp_path / "data.csv"
    df.to_csv(file_path, index=False)

    result_df = task_func(str(file_path))
    assert result_df.equals(df)
    assert file_path.stat().st_size == 0

def test_task_func_with_header(tmp_path):
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    file_path = tmp_path / "data_with_header.csv"
    df.to_csv(file_path, index=False)

    result_df = task_func(str(file_path))
    assert result_df.equals(df)
    assert file_path.stat().st_size == 0

def test_task_func_with_index(tmp_path):
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    file_path = tmp_path / "data_with_index.csv"
    df.to_csv(file_path, index=True)

    result_df = task_func(str(file_path))
    expected_df = df.reset_index(drop=True)
    assert result_df.equals(expected_df)
    assert file_path.stat().st_size == 0