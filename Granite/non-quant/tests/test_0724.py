import csv
import os
import urllib

import pytest
from src_0724 import task_func


def test_task_func():
    url = "https://www.example.com/data"
    csv_file_path = task_func(url)
    assert csv_file_path == 'scraped_data.csv'
    assert os.path.exists(csv_file_path)
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert data[0] == ['Column 1', 'Column 2', 'Column 3']  # Assuming the first row contains column headers
    os.remove(csv_file_path)

def test_task_func_with_invalid_url():
    with pytest.raises(urllib.error.URLError):
        task_func("invalid_url")