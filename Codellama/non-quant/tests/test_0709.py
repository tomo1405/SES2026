import csv
import os

from src_0709 import task_func


def test_task_func():
    # Test with a valid input
    raw_string = "eyJ0ZXN0IjoiYWJjIiwiY29kZSI6Ik1hbmtzIiwiZXhwaXJ5IjoxNjIwMjM5OTk5fQ=="
    filename = "test_file"
    output_dir = "output"
    expected_file_path = os.path.join(output_dir, f'{filename}.csv')

    # Call the function and check the output
    file_path = task_func(raw_string, filename, output_dir)
    assert file_path == expected_file_path

    # Check that the file was created and has the correct contents
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = {row[0]: row[1] for row in reader}
        assert data == {'key1': 'value1', 'key2': 'value2'}

    # Clean up the output directory
    os.remove(file_path)
    os.rmdir(output_dir)