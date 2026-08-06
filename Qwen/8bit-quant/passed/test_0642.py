import pytest
from src_0642 import task_func
import pandas as pd
import os
import tempfile

def test_task_func():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with different names
        open(os.path.join(temp_dir, 'file1.txt'), 'a').close()
        open(os.path.join(temp_dir, 'file2.log'), 'a').close()
        open(os.path.join(temp_dir, 'file3.csv'), 'a').close()

        # Define the pattern to match .txt files
        pattern = r'.*\.txt'

        # Define the output CSV path
        output_csv = os.path.join(temp_dir, 'output.csv')

        # Call the function
        result_df = task_func(pattern, temp_dir, output_csv)

        # Check if the returned DataFrame is correct
        expected_df = pd.DataFrame({'File Path': [os.path.join(temp_dir, 'file1.txt')]})
        pd.testing.assert_frame_equal(result_df, expected_df)

        # Check if the output CSV file is created and contains the correct data
        output_df = pd.read_csv(output_csv)
        pd.testing.assert_frame_equal(output_df, expected_df)

def test_task_func_no_matches():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with different names
        open(os.path.join(temp_dir, 'file1.log'), 'a').close()
        open(os.path.join(temp_dir, 'file2.csv'), 'a').close()

        # Define the pattern to match .txt files
        pattern = r'.*\.txt'

        # Define the output CSV path
        output_csv = os.path.join(temp_dir, 'output.csv')

        # Call the function
        result_df = task_func(pattern, temp_dir, output_csv)

        # Check if the returned DataFrame is empty
        assert result_df.empty

        # Check if the output CSV file is created and is empty
        output_df = pd.read_csv(output_csv)
        assert output_df.empty

def test_task_func_empty_directory():
    # Create a temporary directory without any files
    with tempfile.TemporaryDirectory() as temp_dir:

        # Define the pattern to match .txt files
        pattern = r'.*\.txt'

        # Define the output CSV path
        output_csv = os.path.join(temp_dir, 'output.csv')

        # Call the function
        result_df = task_func(pattern, temp_dir, output_csv)

        # Check if the returned DataFrame is empty
        assert result_df.empty

        # Check if the output CSV file is created and is empty
        output_df = pd.read_csv(output_csv)
        assert output_df.empty