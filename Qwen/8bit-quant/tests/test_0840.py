import pytest
from src_0840 import task_func
import os
import csv

def test_task_func(tmpdir):
    # Create a temporary directory and a file path within it
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_output.csv"))

    # Define parameters
    num_rows = 5
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 42

    # Call the function
    result_path = task_func(file_path, num_rows, gender, countries, seed)

    # Check if the file was created at the correct path
    assert result_path == file_path
    assert os.path.exists(file_path)

    # Read the CSV file and check its contents
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check the number of rows
    assert len(rows) == num_rows

    # Check the headers
    expected_fields = ['Name', 'Age', 'Gender', 'Country']
    assert reader.fieldnames == expected_fields

    # Check the data in each row
    for row in rows:
        assert len(row['Name']) == 5
        assert 20 <= int(row['Age']) <= 60
        assert row['Gender'] in gender
        assert row['Country'] in countries

def test_task_func_with_default_parameters(tmpdir):
    # Create a temporary directory and a file path within it
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_output_default.csv"))

    # Define parameters
    num_rows = 3
    seed = 123

    # Call the function with default parameters
    result_path = task_func(file_path, num_rows, seed=seed)

    # Check if the file was created at the correct path
    assert result_path == file_path
    assert os.path.exists(file_path)

    # Read the CSV file and check its contents
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check the number of rows
    assert len(rows) == num_rows

    # Check the headers
    expected_fields = ['Name', 'Age', 'Gender', 'Country']
    assert reader.fieldnames == expected_fields

    # Check the data in each row
    for row in rows:
        assert len(row['Name']) == 5
        assert 20 <= int(row['Age']) <= 60
        assert row['Gender'] in ['Male', 'Female', 'Non-Binary']
        assert row['Country'] in ['USA', 'UK', 'Canada', 'Australia', 'India']

def test_task_func_with_no_seed(tmpdir):
    # Create a temporary directory and a file path within it
    temp_dir = tmpdir.mkdir("temp")
    file_path = str(temp_dir.join("test_output_no_seed.csv"))

    # Define parameters
    num_rows = 3

    # Call the function without specifying a seed
    result_path = task_func(file_path, num_rows)

    # Check if the file was created at the correct path
    assert result_path == file_path
    assert os.path.exists(file_path)

    # Read the CSV file and check its contents
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check the number of rows
    assert len(rows) == num_rows

    # Check the headers
    expected_fields = ['Name', 'Age', 'Gender', 'Country']
    assert reader.fieldnames == expected_fields

    # Check the data in each row
    for row in rows:
        assert len(row['Name']) == 5
        assert 20 <= int(row['Age']) <= 60
        assert row['Gender'] in ['Male', 'Female', 'Non-Binary']
        assert row['Country'] in ['USA', 'UK', 'Canada', 'Australia', 'India']