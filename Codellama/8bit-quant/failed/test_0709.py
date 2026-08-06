import pytest
from src_0709 import task_func

def test_task_func():
    # Test with a valid input
    raw_string = 'eyJrZXkiOiAidmFsdWUifQ=='
    filename = 'test_file'
    output_dir = 'output'
    expected_file_path = os.path.join(output_dir, f'{filename}.csv')
    expected_data = {'name': 'John Doe', 'age': 30}

    file_path = task_func(raw_string, filename, output_dir)

    assert file_path == expected_file_path

    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = {row[0]: row[1] for row in reader}

    assert data == expected_data

def test_task_func_invalid_input():
    # Test with an invalid input
    raw_string = 'invalid_string'
    filename = 'test_file'
    output_dir = 'output'

    with pytest.raises(ValueError):
        task_func(raw_string, filename, output_dir)