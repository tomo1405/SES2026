import csv
import os
import pandas as pd
from src_0632 import task_func

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})

    # Call the function with a filename
    filename = 'output.csv'
    file_path = task_func(df, filename)

    # Check if the output file exists
    assert os.path.exists(file_path)

    # Check if the output file is a CSV file
    assert file_path.endswith('.csv')

    # Check if the DataFrame was correctly written to the CSV file
    df_written = pd.read_csv(file_path)
    assert df.equals(df_written)

def test_task_func_with_custom_output_dir():
    # Create a sample DataFrame
    df = pd.DataFrame({'col1': [4, 5, 6], 'col2': ['d', 'e', 'f']})

    # Call the function with a custom output directory and filename
    output_dir = '/tmp/output'
    filename = 'custom_output.csv'
    file_path = task_func(df, filename, output_dir)

    # Check if the output file exists
    assert os.path.exists(file_path)

    # Check if the output file is a CSV file
    assert file_path.endswith('.csv')

    # Check if the DataFrame was correctly written to the CSV file
    df_written = pd.read_csv(file_path)
    assert df.equals(df_written)