import csv
import os

import pandas as pd
import pytest
from src_0632 import task_func


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Age': [25, 30]
    })

@pytest.fixture
def temp_output_dir(tmpdir):
    return tmpdir.mkdir("output")

def test_task_func(sample_df, temp_output_dir):
    filename = "test_file.csv"
    result_path = task_func(sample_df, filename, str(temp_output_dir))

    assert os.path.exists(result_path)
    assert os.path.isfile(result_path)

    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    expected_rows = [
        ['Name', 'Age'],
        ['Alice', '25'],
        ['Bob', '30']
    ]
    assert rows == expected_rows

def test_task_func_directory_creation(sample_df, tmpdir):
    filename = "test_file.csv"
    non_existent_dir = os.path.join(tmpdir, "non_existent_output")
    result_path = task_func(sample_df, filename, non_existent_dir)

    assert os.path.exists(non_existent_dir)
    assert os.path.isdir(non_existent_dir)
    assert os.path.isfile(result_path)

def test_task_func_index_false(sample_df, temp_output_dir):
    filename = "test_file.csv"
    result_path = task_func(sample_df, filename, str(temp_output_dir))

    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    assert len(rows) == 3  # Header + 2 data rows
    assert rows[0] == ['Name', 'Age']  # No index column present

def test_task_func_quoting_nonnumeric(sample_df, temp_output_dir):
    filename = "test_file.csv"
    result_path = task_func(sample_df, filename, str(temp_output_dir))

    with open(result_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    assert rows[1][1] == '"25"'  # Age should be quoted as it's non-numeric
    assert rows[2][1] == '"30"'  # Age should be quoted as it's non-numeric