import pytest
from src_0673 import task_func

def test_task_func():
    filename = "test_file.csv"
    with open(filename, "w") as file:
        file.write("1,2,3n4,5,6n7,8,9n")
    expected_output = "9,8,7n6,5,4n3,2,1n"
    actual_output = task_func(filename)
    with open(actual_output, "r") as file:
        actual_data = file.read()
    assert actual_data == expected_output
    with open(filename, "w") as file:
        file.write("1,2,3n4,5,6n7,8,9n")
    expected_output = "An error occurred: Some error message"
    actual_output = task_func(filename)
    assert actual_output == expected_output