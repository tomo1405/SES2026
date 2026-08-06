import pytest
from src_0008 import task_func

def test_task_func():
    csv_file_path = 'path/to/csv/file.csv'
    top_selling_product = task_func(csv_file_path)
    assert top_selling_product == 'Product A'