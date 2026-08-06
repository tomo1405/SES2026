import base64
from cryptography.fernet import Fernet
from src_0027 import task_func
import pytest

@pytest.mark.parametrize("message, encryption_key, expected_output", [
    (
        "This is a secret message",
        "abcdefghijklmnopqrstuvwxyz123456",
        "5d5h6eMhQ293a1Q0Z2hVemhUemhFZ2lK"
    ),
    (
        "Another secret message",
        "1234567890abcdef",
        "5Z2eZ2hFZ2lKemhUemhFZ2lKemhU"
    ),
])
def test_task_func(message, encryption_key, expected_output):
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    actual_output = task_func(message, encryption_key)
    assert actual_output == expected_output