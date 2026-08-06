import pytest
from src_0410 import task_func

def test_task_func_valid_input():
    excel_file_path = 'path/to/excel/file'
    file_name = 'file_name.xlsx'
    column_name = 'column_name'

    result = task_func(excel_file_path, file_name, column_name)

    assert result['mean'] == 0.0
    assert result['median'] == 0.0
    assert result['std_dev'] == 0.0

def test_task_func_invalid_input():
    excel_file_path = 'path/to/excel/file'
    file_name = 'file_name.xlsx'
    column_name = 'invalid_column_name'

    with pytest.raises(ValueError):
        task_func(excel_file_path, file_name, column_name)