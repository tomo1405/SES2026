import pytest
from src_0712 import task_func
import os

def test_task_func(tmpdir):
    # Create a temporary JSON file
    json_file = tmpdir.join("test.json")
    json_data = {"name": "John", "age": 30, "city": "New York"}
    json_file.write(json.dumps(json_data))

    # Create a temporary CSV file path
    csv_file = str(tmpdir.join("test.csv"))

    # Call the function
    result = task_func(str(json_file), csv_file)

    # Check if the function returns the correct CSV file path
    assert result == csv_file

    # Check if the CSV file was created and contains the correct data
    assert os.path.exists(csv_file)
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        values = next(reader)
        assert headers == list(json_data.keys())
        assert values == list(json_data.values())

def test_task_func_with_empty_json(tmpdir):
    # Create a temporary JSON file with empty data
    json_file = tmpdir.join("empty.json")
    json_data = {}
    json_file.write(json.dumps(json_data))

    # Create a temporary CSV file path
    csv_file = str(tmpdir.join("empty.csv"))

    # Call the function
    result = task_func(str(json_file), csv_file)

    # Check if the function returns the correct CSV file path
    assert result == csv_file

    # Check if the CSV file was created and contains the correct data
    assert os.path.exists(csv_file)
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        values = next(reader)
        assert headers == []
        assert values == []

def test_task_func_with_non_existent_json(tmpdir):
    # Use a non-existent JSON file path
    json_file = str(tmpdir.join("non_existent.json"))
    csv_file = str(tmpdir.join("non_existent.csv"))

    # Call the function and expect it to raise a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        task_func(json_file, csv_file)