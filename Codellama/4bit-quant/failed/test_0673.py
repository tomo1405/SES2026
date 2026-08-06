import pytest
from src_0673 import task_func

def test_task_func():
    # Test with a valid file
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        file.write("1,2,3\n4,5,6")
    assert task_func(filename) == filename
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [['3', '2', '1'], ['6', '5', '4']]

    # Test with a non-existent file
    filename = "non_existent_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(filename)

    # Test with a file that cannot be opened
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        file.write("1,2,3\n4,5,6")
    with pytest.raises(PermissionError):
        task_func(filename)