import csv
import os

import pandas as pd
import pytest
from src_0510 import task_func


# Helper function to create temporary CSV files for testing
def create_temp_csv(content, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(content)

# Test case for comparing two identical CSV files
def test_identical_csv_files():
    content = [['name', 'age'], ['Alice', '30'], ['Bob', '25']]
    file_path1 = 'temp_file1.csv'
    file_path2 = 'temp_file2.csv'
    create_temp_csv(content, file_path1)
    create_temp_csv(content, file_path2)

    result_df = task_func(file_path1, file_path2)
    expected_df = pd.DataFrame(columns=['Line Number', 'Status', 'Content'])
    
    assert result_df.equals(expected_df)

    # Clean up temporary files
    os.remove(file_path1)
    os.remove(file_path2)

# Test case for comparing two different CSV files
def test_different_csv_files():
    content1 = [['name', 'age'], ['Alice', '30'], ['Bob', '25']]
    content2 = [['name', 'age'], ['Alice', '31'], ['Charlie', '30']]
    file_path1 = 'temp_file1.csv'
    file_path2 = 'temp_file2.csv'
    create_temp_csv(content1, file_path1)
    create_temp_csv(content2, file_path2)

    result_df = task_func(file_path1, file_path2)
    expected_data = [
        [1, ' ', 'name,age'],
        [2, '-', 'Alice,30'],
        [2, '+', 'Alice,31'],
        [3, '-', 'Bob,25'],
        [4, '+', 'Charlie,30']
    ]
    expected_df = pd.DataFrame(expected_data, columns=['Line Number', 'Status', 'Content'])

    assert result_df.equals(expected_df)

    # Clean up temporary files
    os.remove(file_path1)
    os.remove(file_path2)

# Test case for empty CSV files
def test_empty_csv_files():
    content = []
    file_path1 = 'temp_file1.csv'
    file_path2 = 'temp_file2.csv'
    create_temp_csv(content, file_path1)
    create_temp_csv(content, file_path2)

    with pytest.raises(ValueError) as excinfo:
        task_func(file_path1, file_path2)
    assert "The file 'temp_file1.csv' is empty." in str(excinfo.value)

    # Clean up temporary files
    os.remove(file_path1)
    os.remove(file_path2)

# Test case for one empty and one non-empty CSV file
def test_one_empty_one_non_empty_csv_file():
    content1 = []
    content2 = [['name', 'age'], ['Alice', '30']]
    file_path1 = 'temp_file1.csv'
    file_path2 = 'temp_file2.csv'
    create_temp_csv(content1, file_path1)
    create_temp_csv(content2, file_path2)

    with pytest.raises(ValueError) as excinfo:
        task_func(file_path1, file_path2)
    assert "The file 'temp_file1.csv' is empty." in str(excinfo.value)

    # Clean up temporary files
    os.remove(file_path1)
    os.remove(file_path2)

# Test case for missing CSV file
def test_missing_csv_file():
    file_path1 = 'non_existent_file1.csv'
    file_path2 = 'non_existent_file2.csv'

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(file_path1, file_path2)
    assert "File not found: [Errno 2] No such file or directory: 'non_existent_file1.csv'" in str(excinfo.value)