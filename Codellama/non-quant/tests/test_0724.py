import pytest
from src_0724 import task_func

def test_task_func():
    url = 'https://www.example.com'
    csv_file_path = task_func(url)
    assert os.path.exists(csv_file_path)
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) > 0
        assert len(data[0]) > 0