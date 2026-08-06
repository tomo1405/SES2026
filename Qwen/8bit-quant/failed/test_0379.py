import pytest
from src_0379 import task_func
import pandas as pd
from texttable import Texttable
import os
import glob
import tempfile

def test_task_func_no_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, 'non_existent')
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(non_existent_dir)
        assert str(excinfo.value) == f"The directory '{non_existent_dir}' does not exist."

def test_task_func_no_csv_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(ValueError) as excinfo:
            task_func(temp_dir)
        assert str(excinfo.value) == f"No CSV files found in the directory '{temp_dir}'."

def test_task_func_with_csv_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some CSV files
        csv_file1 = os.path.join(temp_dir, 'file1.csv')
        csv_file2 = os.path.join(temp_dir, 'file2.csv')
        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).to_csv(csv_file1, index=False)
        pd.DataFrame({'C': [5, 6], 'D': [7, 8], 'E': [9, 10]}).to_csv(csv_file2, index=False)

        result = task_func(temp_dir)
        expected_table = Texttable()
        expected_table.add_rows([
            ['File', 'Rows', 'Columns'],
            ['file1.csv', 2, 2],
            ['file2.csv', 2, 3]
        ])
        assert result == expected_table.draw()

def test_task_func_with_empty_csv_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an empty CSV file
        empty_csv_file = os.path.join(temp_dir, 'empty.csv')
        open(empty_csv_file, 'w').close()

        with pytest.raises(pd.errors.EmptyDataError) as excinfo:
            task_func(temp_dir)
        assert str(excinfo.value) == f"Error when reading file '{empty_csv_file}'."