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

def test_task_func_valid_input():
    assert task_func('1f8b08000000000000037363f2f2f2f2e677a69702f6300a301000000') == 'Hello, world!'

def test_task_func_invalid_input():
    assert task_func('1f8b08000000000000037363f2f2f2f2e677a69702f6300a301000001') == 'Error during decompression: Not a gzipped file'