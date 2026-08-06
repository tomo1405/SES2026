from src_0645 import task_func


def test_task_func():
    filename = "test_file.txt"
    data = "test_data"
    password = "test_password"

    encrypted = task_func(filename, data, password)

    assert encrypted == "encrypted_data"