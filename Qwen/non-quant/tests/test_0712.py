import csv
import os
import tempfile

from src_0712 import task_func


def test_task_func():
    # Create a temporary JSON file
    json_content = '{"name": "John", "age": 30, "city": "New York"}'
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_json:
        temp_json.write(json_content)
        temp_json_path = temp_json.name

    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_csv:
        temp_csv_path = temp_csv.name

    # Call the function
    result = task_func(temp_json_path, temp_csv_path)

    # Check if the result is the same as the provided CSV file path
    assert result == temp_csv_path

    # Read the CSV file and check its content
    with open(temp_csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    expected_rows = [
        ['name', 'age', 'city'],
        ['John', '30', 'New York']
    ]

    assert rows == expected_rows

    # Clean up temporary files
    os.remove(temp_json_path)
    os.remove(temp_csv_path)