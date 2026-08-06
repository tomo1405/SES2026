python
import requests
import json
from bs4 import BeautifulSoup
import pytest

def task_func(url: str, file_name: str = "Output.txt") -> str:
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else None
    data = {"title": title}
    json_data = json.dumps(data)
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(json_data + "\n")
    return file_name

def test_task_func():
    # Test case 1: Valid URL
    url = "https://www.google.com"
    file_name = "test_output.txt"
    result = task_func(url, file_name)
    assert result == file_name
    # Test case 2: Invalid URL
    url = "https://www.google.com/invalid"
    file_name = "test_output.txt"
    with pytest.raises(requests.exceptions.RequestException):
        task_func(url, file_name)
    # Test case 3: Valid URL with no title
    url = "https://www.python.org"
    file_name = "test_output.txt"
    result = task_func(url, file_name)
    assert result == file_name
    # Test case 4: Valid URL with no file name
    url = "https://www.python.org"
    result = task_func(url)
    assert result == "Output.txt"
    # Test case 5: Valid URL with file name ending with .txt
    url = "https://www.python.org"
    file_name = "test_output.txt"
    result = task_func(url, file_name)
    assert result == file_name
    # Test case 6: Valid URL with file name ending with .json
    url = "https://www.python.org"
    file_name = "test_output.json"
    result = task_func(url, file_name)
    assert result == file_name
    # Test case 7: Valid URL with file name ending with .csv
    url = "https://www.python.org"
    file_name = "test_output.csv"
    with pytest.raises(ValueError):
        task_func(url, file_name)