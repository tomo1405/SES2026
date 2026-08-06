python
import json
import csv
import os
import base64
import pytest

def task_func(raw_string, filename, output_dir):
    # Decode the string and load the data
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    data = json.loads(decoded_string)

    # Prepare the output directory
    os.makedirs(output_dir, exist_ok=True)

    # Prepare the file path
    file_path = os.path.join(output_dir, f'{filename}.csv')

    # Save the data to the file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])

    return file_path

def test_task_func():
    # Test case 1: Valid input
    raw_string = 'eyJmb28iOiAyLCAiYWdlIjogMSwgInR5cGUiOiAidGV4dCIsICJ0eXBlIjogInRleHQiLCAidmFsdWUiOiAidGVzdCJ9'
    filename = 'test'
    output_dir = 'output'
    expected_file_path = os.path.join(output_dir, f'{filename}.csv')
    assert task_func(raw_string, filename, output_dir) == expected_file_path

    # Test case 2: Invalid input (empty string)
    with pytest.raises(ValueError):
        task_func('', 'test', 'output')

    # Test case 3: Invalid input (invalid JSON)
    with pytest.raises(json.JSONDecodeError):
        task_func('invalid_json', 'test', 'output')

    # Test case 4: Invalid input (invalid output directory)
    with pytest.raises(NotADirectoryError):
        task_func('eyJmb28iOiAyLCAiYWdlIjogMSwgInR5cGUiOiAidGV4dCIsICJ0eXBlIjogInRleHQiLCAidmFsdWUiOiAidGVzdCJ9', 'test', 'invalid_dir')