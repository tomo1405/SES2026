import os
import csv
from openpyxl import load_workbook
import pytest

def task_func(file_name, excel_file_path, csv_file_path) -> str:

    excel_file = os.path.join(excel_file_path, file_name)
    # Check if the Excel file exists
    if not os.path.isfile(excel_file):
        raise FileNotFoundError(f"[Errno 2] No such file or directory: '{excel_file}'")

    workbook = load_workbook(filename=excel_file, read_only=True)
    sheet = workbook.active

    data = [[cell.value for cell in row] for row in sheet.iter_rows()]

    csv_file_name = os.path.splitext(file_name)[0] + '.csv'
    csv_file = os.path.join(csv_file_path, csv_file_name)

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return csv_file_name

def test_task_func():
    file_name = 'example.xlsx'
    excel_file_path = '/path/to/excel/files'
    csv_file_path = '/path/to/csv/files'

    with pytest.raises(FileNotFoundError):
        task_func(file_name, excel_file_path, csv_file_path)

    file_name = 'example.xlsx'
    excel_file_path = '/path/to/excel/files'
    csv_file_path = '/path/to/csv/files'

    csv_file_name = task_func(file_name, excel_file_path, csv_file_path)
    assert csv_file_name == 'example.csv'