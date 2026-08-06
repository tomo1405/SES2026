import pytest
from src_0835 import task_func

def test_task_func():
    compressed_hex = "1f8b0808f5b2220200000022540022751f8b0808f5b222020000002254002275"
    expected_output = "Hello, world!"

    actual_output = task_func(compressed_hex)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_hex():
    compressed_hex = "invalid_hex"
    expected_output = "Error during decompression: Error - Not a zlib file"

    actual_output = task_func(compressed_hex)

    assert actual_output == expected_output, "Output does not match expected output"