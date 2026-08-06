python
import json
import os
import pytest

def task_func(filename, data):
    try:
        # Write the dictionary to the file as JSON
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        # Verify the file exists after writing, using os.path.exists
        file_exists = os.path.exists(filename)
        if not file_exists:
            return False, None

        # Read the file back to verify content
        with open(filename, 'r') as f:
            written_data = json.load(f)
            if written_data != data:
                return False, None

        return True, written_data
    except Exception as e:
        return False, None

def test_task_func():
    # Test case 1: Valid input
    data = {'name': 'John', 'age': 30}
    filename = 'test.json'
    assert task_func(filename, data) == (True, data)

    # Test case 2: Invalid input (empty data)
    data = {}
    filename = 'test.json'
    assert task_func(filename, data) == (False, None)

    # Test case 3: Invalid input (non-existent file)
    data = {'name': 'John', 'age': 30}
    filename = 'nonexistent.json'
    assert task_func(filename, data) == (False, None)

    # Test case 4: Invalid input (invalid JSON)
    data = {'name': 'John', 'age': 30}
    filename = 'invalid.json'
    with open(filename, 'w') as f:
        f.write('invalid JSON')
    assert task_func(filename, data) == (False, None)

    # Test case 5: Invalid input (invalid data)
    data = {'name': 'John', 'age': '30'}
    filename = 'invalid.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
    assert task_func(filename, data) == (False, None)

    # Test case 6: Invalid input (invalid file extension)
    data = {'name': 'John', 'age': 30}
    filename = 'test.txt'
    assert task_func(filename, data) == (False, None)