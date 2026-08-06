import pytest
from src_0840 import task_func
import os
import csv

def test_task_func(tmpdir):
    # Create a temporary directory and file path
    temp_dir = tmpdir.mkdir("temp")
    file_path = temp_dir.join("test_output.csv")

    # Define test parameters
    num_rows = 10
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 42

    # Call the function
    result_path = task_func(str(file_path), num_rows, gender, countries, seed)

    # Check if the file was created
    assert os.path.exists(result_path)

    # Read the CSV file and check its contents
    with open(result_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check the number of rows
    assert len(rows) == num_rows

    # Check the fields
    for row in rows:
        assert set(row.keys()) == {'Name', 'Age', 'Gender', 'Country'}

    # Check the data types and values
    for row in rows:
        assert isinstance(row['Name'], str)
        assert len(row['Name']) == 5
        assert all(c.isalpha() for c in row['Name'])
        assert isinstance(row['Age'], int)
        assert 20 <= row['Age'] <= 60
        assert row['Gender'] in gender
        assert row['Country'] in countries

# Test with a different seed to ensure reproducibility
def test_task_func_reproducibility(tmpdir):
    # Create a temporary directory and file path
    temp_dir = tmpdir.mkdir("temp")
    file_path = temp_dir.join("test_output_reproducible.csv")

    # Define test parameters
    num_rows = 10
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 42

    # Call the function twice with the same seed
    result_path_1 = task_func(str(file_path), num_rows, gender, countries, seed)
    result_path_2 = task_func(str(file_path), num_rows, gender, countries, seed)

    # Read the CSV files
    with open(result_path_1, newline='') as csvfile1:
        reader1 = csv.DictReader(csvfile1)
        rows1 = list(reader1)

    with open(result_path_2, newline='') as csvfile2:
        reader2 = csv.DictReader(csvfile2)
        rows2 = list(reader2)

    # Check if the contents are identical
    assert rows1 == rows2