import pytest
from src_0592 import task_func

def test_task_func():
    hours = 10  # You can adjust this value as needed
    file_path, ax = task_func(hours)
    assert file_path == 'custom_data.csv'
    assert ax is not None

if __name__ == '__main__':
    pytest.main()