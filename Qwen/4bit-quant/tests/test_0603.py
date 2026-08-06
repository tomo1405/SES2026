import os

import pandas as pd
from src_0603 import task_func


def test_task_func_output_directory_exists():
    # Create a temporary directory for testing
    temp_dir = 'temp_test_dir'
    file_path = os.path.join(temp_dir, 'test_file.tsv')

    # Call the function
    task_func(file_path, output_dir=temp_dir)

    # Check if the directory exists
    assert os.path.exists(temp_dir), "Output directory does not exist"

    # Clean up
    os.rmdir(temp_dir)

def test_task_func_file_creation():
    # Create a temporary directory for testing
    temp_dir = 'temp_test_dir'
    file_path = os.path.join(temp_dir, 'test_file.tsv')

    # Call the function
    task_func(file_path, output_dir=temp_dir)

    # Check if the file is created
    assert os.path.isfile(file_path), "File was not created"

    # Clean up
    os.remove(file_path)
    os.rmdir(temp_dir)

def test_task_func_file_content():
    # Create a temporary directory for testing
    temp_dir = 'temp_test_dir'
    file_path = os.path.join(temp_dir, 'test_file.tsv')

    # Call the function
    task_func(file_path, output_dir=temp_dir)

    # Read the content of the file
    with open(file_path, 'r') as f:
        content = f.read()

    # Check if the content is not empty
    assert content.strip(), "File content is empty"

    # Clean up
    os.remove(file_path)
    os.rmdir(temp_dir)

def test_task_func_file_format():
    # Create a temporary directory for testing
    temp_dir = 'temp_test_dir'
    file_path = os.path.join(temp_dir, 'test_file.tsv')

    # Call the function
    task_func(file_path, output_dir=temp_dir)

    # Read the content of the file into a DataFrame
    df = pd.read_csv(file_path, sep='\t', header=None)

    # Check if the DataFrame has the correct shape
    assert df.shape == (10, 10), "DataFrame shape is incorrect"

    # Check if all elements in the DataFrame are letters
    assert all(df.applymap(lambda x: x.isalpha()).all()), "Not all elements are letters"

    # Clean up
    os.remove(file_path)
    os.rmdir(temp_dir)