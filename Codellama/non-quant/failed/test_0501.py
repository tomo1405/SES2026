import pytest
from src_0501 import task_func


def test_task_func():
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 25},
        {'ID': 2, 'Name': 'Jane', 'Age': 30},
        {'ID': 3, 'Name': 'Jim', 'Age': 35},
    ]
    filename = 'test_data.xls'

    # Test that the function returns the correct file path
    assert task_func(values, filename) == os.path.abspath(filename)

    # Test that the file is created and has the correct contents
    assert os.path.exists(filename)
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert lines[0] == 'ID,Name,Age\n'
        assert lines[1] == '1,John,25\n'
        assert lines[2] == '2,Jane,30\n'
        assert lines[3] == '3,Jim,35\n'

    # Test that the function raises an error if the file already exists
    with pytest.raises(FileExistsError):
        task_func(values, filename)

    # Test that the function raises an error if the values are not a list of dictionaries
    with pytest.raises(TypeError):
        task_func('not a list', filename)

    # Test that the function raises an error if the values are empty
    with pytest.raises(ValueError):
        task_func([], filename)