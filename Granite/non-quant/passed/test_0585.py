import pytest
from src_0585 import task_func

@pytest.mark.parametrize("url, expected_pub_key, expected_signed_hash, expected_hash_value", [
    ("https://example.com", "<pub_key>", "<signed_hash>", "<hash_value>"),
    ("https://example.org", "<pub_key>", "<signed_hash>", "<hash_value>"),
])
def test_task_func(url, expected_pub_key, expected_signed_hash, expected_hash_value):
    pub_key, signed_hash, hash_value = task_func(url)
    assert pub_key == expected_pub_key
    assert signed_hash == expected_signed_hash
    assert hash_value == expected_hash_value