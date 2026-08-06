import pytest
from src_0906 import task_func

def test_task_func_with_no_files(tmpdir):
    # Create a temporary directory with no files
    empty_dir = tmpdir.mkdir("empty")
    
    # Call the function and check that it returns an empty dictionary
    result = task_func(str(empty_dir))
    assert result == {}

def test_task_func_with_single_csv_file(tmpdir):
    # Create a temporary directory with a single CSV file
    single_csv_dir = tmpdir.mkdir("single_csv")
    single_csv_file = single_csv_dir.join("data.csv")
    single_csv_file.write("name,age\nAlice,30")

    # Call the function and check that it returns the correct data
    result = task_func(str(single_csv_dir))
    expected = {
        "data": [["name", "age"], ["Alice", "30"]]
    }
    assert result == expected

def test_task_func_with_multiple_csv_files(tmpdir):
    # Create a temporary directory with multiple CSV files
    multiple_csv_dir = tmpdir.mkdir("multiple_csv")
    file1 = multiple_csv_dir.join("file1.csv")
    file2 = multiple_csv_dir.join("file2.csv")
    file1.write("name,age\nBob,25")
    file2.write("name,age\nCharlie,35")

    # Call the function and check that it returns the correct data
    result = task_func(str(multiple_csv_dir))
    expected = {
        "file1": [["name", "age"], ["Bob", "25"]],
        "file2": [["name", "age"], ["Charlie", "35"]]
    }
    assert result == expected

def test_task_func_with_non_csv_files(tmpdir):
    # Create a temporary directory with non-CSV files
    non_csv_dir = tmpdir.mkdir("non_csv")
    non_csv_file = non_csv_dir.join("data.txt")
    non_csv_file.write("This is a text file.")

    # Call the function and check that it returns an empty dictionary
    result = task_func(str(non_csv_dir))
    assert result == {}

def test_task_func_with_custom_extension(tmpdir):
    # Create a temporary directory with a custom extension file
    custom_ext_dir = tmpdir.mkdir("custom_ext")
    custom_ext_file = custom_ext_dir.join("data.json")
    custom_ext_file.write('{"name": "Eve", "age": 40}')

    # Call the function with a custom extension and check that it returns an empty dictionary
    result = task_func(str(custom_ext_dir), file_extension='.json')
    assert result == {}