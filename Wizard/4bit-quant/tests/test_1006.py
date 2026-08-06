python
import urllib.request
import zipfile
import os
import urllib.error
import pytest

def task_func(
    url: str,
    save_path: str = "downloaded_file.zip",
    extract_path: str = "extracted_files",
) -> str:
    try:
        # Check if save_path already exists, if so, remove it
        if os.path.exists(save_path):
            os.remove(save_path)

        # Download the file from the URL
        urllib.request.urlretrieve(url, save_path)

        # Create the extraction directory if it doesn't exist
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        # Extract the zip file
        with zipfile.ZipFile(save_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        # Remove the downloaded zip file
        os.remove(save_path)

        return extract_path
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"

def test_task_func():
    # Test case 1: Download a zip file from a valid URL and extract it
    url = "https://www.example.com/example.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    assert task_func(url, save_path, extract_path) == "extracted_files"

    # Test case 2: Download a zip file from an invalid URL and return an error message
    url = "https://www.example.com/invalid.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    assert task_func(url, save_path, extract_path) == "URL Error: Not Found"

    # Test case 3: Download a zip file from a valid URL, extract it, and remove the downloaded zip file
    url = "https://www.example.com/example.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    task_func(url, save_path, extract_path)
    assert not os.path.exists(save_path)

    # Test case 4: Download a zip file from a valid URL, extract it, and remove the extracted files
    url = "https://www.example.com/example.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    task_func(url, save_path, extract_path)
    assert not os.path.exists(extract_path)

    # Test case 5: Download a zip file from a valid URL, extract it, and remove the downloaded zip file and extracted files
    url = "https://www.example.com/example.zip"
    save_path = "downloaded_file.zip"
    extract_path = "extracted_files"
    task_func(url, save_path, extract_path)
    assert not os.path.exists(save_path)
    assert not os.path.exists(extract_path)