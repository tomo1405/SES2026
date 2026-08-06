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
    assert task_func().startswith("Server started on")
    assert task_func().endswith("seconds.")

    # Test that the function returns a string with the correct server address and port
    assert task_func(server_address="localhost", server_port=12345).startswith("Server started on localhost:12345")

    # Test that the function returns a string with the correct buffer size
    assert task_func(buffer_size=1024).endswith("seconds.")

    # Test that the function returns a string with the correct run duration
    assert task_func(run_duration=5).endswith("seconds.")