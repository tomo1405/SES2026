import csv
import os
import tempfile

import pandas as pd
from src_0632 import task_func


def test_task_func():
    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define a sample DataFrame
        data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        df = pd.DataFrame(data)
        
        # Define the filename
        filename = 'test_output.csv'
        
        # Call the function
        result_path = task_func(df, filename, output_dir=temp_dir)
        
        # Check if the file exists
        assert os.path.exists(result_path)
        
        # Read the CSV file and check its contents
        with open(result_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        
        # Check the header and data
        assert rows[0] == ['Name', 'Age']
        assert rows[1] == ['"Alice"', '"25"']
        assert rows[2] == ['"Bob"', '"30"']

def test_task_func_nonexistent_directory():
    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define a non-existent subdirectory
        non_existent_subdir = os.path.join(temp_dir, 'non_existent')
        
        # Define a sample DataFrame
        data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        df = pd.DataFrame(data)
        
        # Define the filename
        filename = 'test_output.csv'
        
        # Call the function
        result_path = task_func(df, filename, output_dir=non_existent_subdir)
        
        # Check if the file exists
        assert os.path.exists(result_path)
        
        # Read the CSV file and check its contents
        with open(result_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        
        # Check the header and data
        assert rows[0] == ['Name', 'Age']
        assert rows[1] == ['"Alice"', '"25"']
        assert rows[2] == ['"Bob"', '"30"']