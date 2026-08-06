import base64
from cryptography.fernet import Fernet
from src_0027 import task_func
import pytest

@pytest.mark.parametrize("message, encryption_key, expected_output", [
    (
        "This is a secret message",
        "abcdefghijklmnopqrstuvwxyz123456",
        "5v2h3m4y5v6i7m8n9o0p1q2r3s4t"
    ),
    (
        "Another secret message",
        "1234567890abcdef",
        "6r8s9t0u1v2w3x4y5z6a7b8c9d0e"
    ),
])
def test_task_func(message, encryption_key, expected_output):
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    actual_output = task_func(message, encryption_key)
    assert actual_output == expected_output