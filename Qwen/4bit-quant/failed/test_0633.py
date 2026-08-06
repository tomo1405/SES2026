import pytest
from src_0633 import task_func
import os
import pandas as pd
import json
import tempfile

def test_task_func():
    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set the temporary directory as the output directory
        os.environ['OUTPUT_DIR'] = temp_dir

        # Create a sample DataFrame
        data = {
            'name': ['Alice', 'Bob'],
            'age': [25, 30]
        }
        df = pd.DataFrame(data)

        # Define a filename
        filename = 'test_output.jsonl'

        # Call the function
        result_path = task_func(df, filename)

        # Check if the file was created
        assert os.path.exists(result_path), "The file was not created."

        # Read the content of the file
        with open(result_path, 'r') as file:
            lines = file.readlines()

        # Check the number of lines
        assert len(lines) == 2, "The number of lines in the file is incorrect."

        # Check the content of each line
        expected_records = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30}
        ]
        for line, expected_record in zip(lines, expected_records):
            assert json.loads(line.strip()) == expected_record, "The content of the file is incorrect."

        # Clean up the environment variable
        del os.environ['OUTPUT_DIR']