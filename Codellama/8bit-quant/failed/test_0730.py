import pytest
from src_0730 import task_func

def test_task_func():
    # Test that the function returns the correct value
    strings = ["hello", "world"]
    filename = "test_file.pkl"
    assert task_func(strings, filename) == strings

    # Test that the function creates and deletes the file correctly
    assert os.path.exists(filename)
    assert not os.path.exists(filename)

    # Test that the function raises an error if the file cannot be opened
    with pytest.raises(FileNotFoundError):
        task_func(strings, "non_existent_file.pkl")