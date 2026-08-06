import pytest
from src_1006 import task_func

def test_task_func():
    # Test that the function returns the expected path when the download is successful
    url = "https://www.example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    expected_path = extract_path
    assert task_func(url, save_path, extract_path) == expected_path

    # Test that the function returns the expected error message when the download fails
    url = "https://www.example.com/file.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    expected_error = "URL Error: <error message>"
    with pytest.raises(urllib.error.URLError) as e:
        task_func(url, save_path, extract_path)
    assert str(e.value) == expected_error