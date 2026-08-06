import pytest
from src_0207 import task_func
import os
import json
import tempfile

def test_task_func_with_valid_csv():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w+', newline='') as temp_csv:
        temp_csv.write('name,age\nAlice,30\nBob,25')
        temp_csv.flush()
        temp_csv_name = temp_csv.name

    try:
        # Call the function with the temporary CSV file
        result_json_name = task_func(temp_csv_name)

        # Check if the JSON file is created
        assert os.path.exists(result_json_name)

        # Check if the content of the JSON file is correct
        with open(result_json_name, 'r') as json_file:
            data = json.load(json_file)
            assert data == [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]

    finally:
        # Clean up temporary files
        os.remove(temp_csv_name)
        if os.path.exists(result_json_name):
            os.remove(result_json_name)

def test_task_func_with_non_existent_file():
    # Use a non-existent file name
    non_existent_file_name = 'non_existent.csv'

    # Check if the function raises FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(non_existent_file_name)

    assert str(excinfo.value) == "File does not exist."

def test_task_func_with_empty_csv():
    # Create a temporary empty CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w+', newline='') as temp_csv:
        temp_csv.flush()
        temp_csv_name = temp_csv.name

    try:
        # Call the function with the empty CSV file
        result_json_name = task_func(temp_csv_name)

        # Check if the JSON file is created
        assert os.path.exists(result_json_name)

        # Check if the content of the JSON file is empty
        with open(result_json_name, 'r') as json_file:
            data = json.load(json_file)
            assert data == []

    finally:
        # Clean up temporary files
        os.remove(temp_csv_name)
        if os.path.exists(result_json_name):
            os.remove(result_json_name)