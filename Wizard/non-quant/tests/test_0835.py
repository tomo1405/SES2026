python
import binascii
import io
import gzip
import pytest

def task_func(compressed_hex):
    try:
        compressed_bytes = binascii.unhexlify(compressed_hex)
        decompressed_bytes = gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes)).read()
        decoded_string = decompressed_bytes.decode('utf-8')
        return decoded_string
    except gzip.BadGzipFile as e:
        return "Error during decompression: " + str(e)

def test_task_func():
    # Test case 1: Valid input
    compressed_hex = "1f8b0800000000000003736b0a000000"
    expected_output = "Hello, world!"
    assert task_func(compressed_hex) == expected_output

    # Test case 2: Invalid input (not a valid gzip file)
    compressed_hex = "1f8b0800000000000003736b0a00000000"
    expected_output = "Error during decompression: Not a gzipped file"
    assert task_func(compressed_hex) == expected_output