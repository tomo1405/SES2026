import pytest
from src_0642 import task_func
import os
import pandas as pd

@pytest.fixture
def temp_dir(tmpdir):
    return tmpdir.mkdir("test_dir")

@pytest.fixture
def create_files(temp_dir):
    temp_dir.join("file1.txt").write("content1")
    temp_dir.join("file2.log").write("content2")
    temp_dir.join("file3.csv").write("content3")
    return temp_dir

def test_task_func(create_files):
    pattern = r".*\.txt"
    directory = str(create_files)
    output_csv = "output.csv"

    result_df = task_func(pattern, directory, output_csv)

    expected_df = pd.DataFrame({
        'File Path': [os.path.join(directory, 'file1.txt')]
    })

    assert result_df.equals(expected_df)

    # Check if the CSV file was created and contains the correct data
    assert os.path.exists(output_csv)
    df_from_csv = pd.read_csv(output_csv)
    assert df_from_csv.equals(expected_df)

def test_task_func_no_matches(create_files):
    pattern = r".*\.json"
    directory = str(create_files)
    output_csv = "output.csv"

    result_df = task_func(pattern, directory, output_csv)

    expected_df = pd.DataFrame(columns=['File Path'])

    assert result_df.equals(expected_df)

    # Check if the CSV file was created and is empty
    assert os.path.exists(output_csv)
    df_from_csv = pd.read_csv(output_csv)
    assert df_from_csv.empty