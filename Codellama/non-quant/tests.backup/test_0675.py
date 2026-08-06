import pytest
from src_0675 import task_func

def test_task_func_with_valid_file():
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        file.write("1,2,3\n4,5,6")

    result = task_func(filename)

    assert result == filename
    with open(filename, 'r') as file:
        data = file.read()
        assert data == "3,2,1\n6,5,4"

def test_task_func_with_invalid_file():
    filename = "invalid_file.csv"
    result = task_func(filename)

    assert result == filename
    with pytest.raises(FileNotFoundError):
        with open(filename, 'r') as file:
            file.read()

def test_task_func_with_empty_file():
    filename = "empty_file.csv"
    with open(filename, 'w') as file:
        file.write("")

    result = task_func(filename)

    assert result == filename
    with open(filename, 'r') as file:
        data = file.read()
        assert data == ""