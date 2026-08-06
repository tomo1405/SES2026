import pytest
from src_0566 import task_func

def test_task_func(tmp_path):
    # Create a temporary file with some content
    test_file = tmp_path / "testfile.so"
    test_file.write_bytes(b"Sample content")

    # Call the function with the path to the temporary file
    result = task_func(str(test_file))

    # Assert that the result is the name of the shared library
    assert result == "_name"

    # Check that the MD5 and SHA256 hashes are printed
    captured = capsys.readouterr()
    assert "MD5 Hash: 9e107d9d372bb6826bd81d3542a419d6" in captured.out
    assert "SHA256 Hash: 5d41402abc4b2a76b9719d911017c592" in captured.out