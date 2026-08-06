from src_1133 import task_func


def test_task_func():
    password = "password"
    PREFIX = "ME"
    SALT_LENGTH = 16

    result = task_func(password, PREFIX, SALT_LENGTH)

    assert result == "MEpassword" + salt.hex()