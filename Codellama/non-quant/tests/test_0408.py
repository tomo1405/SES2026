import pytest
from src_0408 import task_func

def test_task_func_valid_input():
    file_name = 'test_file.xlsx'
    excel_file_path = 'path/to/excel/file'
    csv_file_path = 'path/to/csv/file'

    csv_file_name = task_func(file_name, excel_file_path, csv_file_path)

    assert csv_file_name == 'test_file.csv'

def test_task_func_invalid_input():
    file_name = 'test_file.xlsx'
    excel_file_path = 'path/to/excel/file'
    csv_file_path = 'path/to/csv/file'

    with pytest.raises(FileNotFoundError):
        task_func(file_name, excel_file_path, csv_file_path)