import pytest
from src_0642 import task_func
import os
import pandas as pd
import tempfile

def test_task_func_no_matches():
    with tempfile.TemporaryDirectory() as temp_dir:
        pattern = r"non_existent_pattern"
        output_csv = os.path.join(temp_dir, "output.csv")
        result_df = task_func(pattern, temp_dir, output_csv)
        assert result_df.empty
        assert not os.path.exists(output_csv)

def test_task_func_single_match():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = "test_file.txt"
        open(os.path.join(temp_dir, test_file), 'a').close()
        pattern = r"test_file\.txt"
        output_csv = os.path.join(temp_dir, "output.csv")
        result_df = task_func(pattern, temp_dir, output_csv)
        assert len(result_df) == 1
        assert result_df.iloc[0]['File Path'] == os.path.join(temp_dir, test_file)
        assert os.path.exists(output_csv)
        loaded_df = pd.read_csv(output_csv)
        assert loaded_df.equals(result_df)

def test_task_func_multiple_matches():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_files = ["file1.txt", "file2.txt", "file3.log"]
        for file in test_files:
            open(os.path.join(temp_dir, file), 'a').close()
        pattern = r".*\.txt"
        output_csv = os.path.join(temp_dir, "output.csv")
        result_df = task_func(pattern, temp_dir, output_csv)
        assert len(result_df) == 2
        expected_paths = [os.path.join(temp_dir, file) for file in ["file1.txt", "file2.txt"]]
        assert all(path in result_df['File Path'].values for path in expected_paths)
        assert os.path.exists(output_csv)
        loaded_df = pd.read_csv(output_csv)
        assert loaded_df.equals(result_df)

def test_task_func_nested_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        nested_dir = os.path.join(temp_dir, "nested")
        os.makedirs(nested_dir)
        test_files = ["file1.txt", "file2.txt", "file3.log"]
        for file in test_files:
            open(os.path.join(nested_dir, file), 'a').close()
        pattern = r".*\.txt"
        output_csv = os.path.join(temp_dir, "output.csv")
        result_df = task_func(pattern, temp_dir, output_csv)
        assert len(result_df) == 2
        expected_paths = [os.path.join(nested_dir, file) for file in ["file1.txt", "file2.txt"]]
        assert all(path in result_df['File Path'].values for path in expected_paths)
        assert os.path.exists(output_csv)
        loaded_df = pd.read_csv(output_csv)
        assert loaded_df.equals(result_df)