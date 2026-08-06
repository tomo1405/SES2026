import pytest
from src_0408 import task_func
import os
import csv
from openpyxl import Workbook

def test_task_func(tmpdir):
    # Create a temporary Excel file
    excel_dir = tmpdir.mkdir("excel")
    excel_file_path = str(excel_dir)
    excel_file_name = "test.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.append([1, 2, 3])
    ws.append([4, 5, 6])
    wb.save(os.path.join(excel_file_path, excel_file_name))

    # Create a temporary CSV directory
    csv_dir = tmpdir.mkdir("csv")
    csv_file_path = str(csv_dir)

    # Call the function
    result = task_func(excel_file_name, excel_file_path, csv_file_path)

    # Check if the CSV file is created
    expected_csv_file_name = "test.csv"
    assert result == expected_csv_file_name
    assert os.path.isfile(os.path.join(csv_file_path, expected_csv_file_name))

    # Check the content of the CSV file
    with open(os.path.join(csv_file_path, expected_csv_file_name), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [[1, 2, 3], [4, 5, 6]]

def test_task_func_file_not_found(tmpdir):
    # Create a temporary Excel directory without any files
    excel_dir = tmpdir.mkdir("excel")
    excel_file_path = str(excel_dir)

    # Create a temporary CSV directory
    csv_dir = tmpdir.mkdir("csv")
    csv_file_path = str(csv_dir)

    # Call the function and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.xlsx", excel_file_path, csv_file_path)
    assert "[Errno 2] No such file or directory: '/tmp/pytest-of-user/pytest-0/test_task_func_file_not_found0/excel/non_existent_file.xlsx'" in str(excinfo.value)