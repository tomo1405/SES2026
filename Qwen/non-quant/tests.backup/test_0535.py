import pytest
from src_0535 import task_func
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def test_task_func():
    # Generate a private key for testing
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Define test cases
    test_cases = [
        ("10", 2, 16, private_key, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"),
        ("FF", 16, 2, private_key, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"),
        ("123456", 10, 8, private_key, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"),
    ]

    for num, from_base, to_base, private_key, alphabet in test_cases:
        result = task_func(num, from_base, to_base, private_key, alphabet)
        assert isinstance(result, str), "The result should be a string"
        assert len(result) > 0, "The result should not be empty"

# Run the tests
if __name__ == "__main__":
    pytest.main()