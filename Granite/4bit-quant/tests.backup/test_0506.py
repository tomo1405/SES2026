import hashlib
import hmac
import pytest

def task_func(secret, message):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def test_task_func():
    secret = "my_secret_key"
    message = "my_message"
    expected_result = "4f19f09b85d7218f2e4249d9b0087331f9e2d78e9f9e49d38919c35e5d3c928d"
    result = task_func(secret, message)
    assert result == expected_result, "The result does not match the expected value"

if __name__ == "__main__":
    pytest.main()