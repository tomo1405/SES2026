import pytest
from src_0566 import task_func

def test_task_func_md5_hash(mocker, tmp_path):
    # Create a temporary file and write some data to it
    test_data = b'hello world'
    test_file = tmp_path / "test_file.bin"
    test_file.write_bytes(test_data)

    # Mock the ctypes.CDLL call to avoid loading a real library
    mock_lib = mocker.Mock()
    mock_lib._name = "mock_library_name"
    mocker.patch('src_0566.ctypes.CDLL', return_value=mock_lib)

    # Capture stdout to check the printed hash values
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    result = task_func(str(test_file))

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check the returned value
    assert result == "mock_library_name"

    # Check the printed MD5 hash
    expected_md5 = hashlib.md5(test_data).hexdigest()
    assert f'MD5 Hash: {expected_md5}\n' in captured_output.getvalue()

    # Check the printed SHA256 hash
    expected_sha256 = hashlib.sha256(test_data).hexdigest()
    assert f'SHA256 Hash: {expected_sha256}\n' in captured_output.getvalue()