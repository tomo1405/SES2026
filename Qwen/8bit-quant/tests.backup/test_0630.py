import pytest
from src_0630 import task_func
import pandas as pd
import os

@pytest.fixture
def dataset():
    return [pd.DataFrame({'A': [1, 2], 'B': [3, 4]}), pd.DataFrame({'C': [5, 6], 'D': [7, 8]})]

@pytest.fixture
def filename():
    return "test_output.csv"

@pytest.fixture
def output_dir(tmpdir):
    return tmpdir.mkdir("output")

def test_task_func_creates_directory_and_file(dataset, filename, output_dir):
    task_func(dataset, filename, str(output_dir))
    assert os.path.exists(os.path.join(str(output_dir), filename))

def test_task_func_writes_correct_content(dataset, filename, output_dir):
    task_func(dataset, filename, str(output_dir))
    with open(os.path.join(str(output_dir), filename), 'r') as f:
        content = f.read()
    expected_content = ("A,B\n1,3\n2,4\n------\nC,D\n5,6\n7,8\n")
    assert content == expected_content

def test_task_func_handles_single_dataframe(dataset, filename, output_dir):
    single_df_dataset = dataset[:1]
    task_func(single_df_dataset, filename, str(output_dir))
    with open(os.path.join(str(output_dir), filename), 'r') as f:
        content = f.read()
    expected_content = "A,B\n1,3\n2,4\n"
    assert content == expected_content

def test_task_func_no_extra_newlines(dataset, filename, output_dir):
    task_func(dataset, filename, str(output_dir))
    with open(os.path.join(str(output_dir), filename), 'r') as f:
        lines = f.readlines()
    assert lines[-1] != '\n'

def test_task_func_timing(dataset, filename, output_dir, monkeypatch):
    mock_time = [0, 1]  # Start and end times
    monkeypatch.setattr(time, 'time', lambda: mock_time.pop(0))
    task_func(dataset, filename, str(output_dir))
    with open(os.path.join(str(output_dir), filename), 'r') as f:
        lines = f.readlines()
    assert lines[-1].startswith("Operation completed in 1.0 seconds.")