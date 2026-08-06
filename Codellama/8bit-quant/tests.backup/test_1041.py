import pytest
from src_1041 import task_func


def test_task_func():
    # Test that the function returns a string
    assert isinstance(task_func(), str)

    # Test that the function raises a ValueError if the server address is invalid
    with pytest.raises(ValueError):
        task_func(server_address="invalid_address")

    # Test that the function raises a ValueError if the server port is invalid
    with pytest.raises(ValueError):
        task_func(server_port=0)

    # Test that the function raises a ValueError if the buffer size is invalid
    with pytest.raises(ValueError):
        task_func(buffer_size=0)

    # Test that the function raises a ValueError if the run duration is invalid
    with pytest.raises(ValueError):
        task_func(run_duration=0)

    # Test that the function returns a string with the correct format
    assert task_func(server_address="localhost", server_port=12345, buffer_size=1024, run_duration=5) == "Server started on localhost:12345. Ran for 5 seconds."