import pytest
from src_0408 import task_func
import os
import csv
from openpyxl import Workbook

# Helper function to create a temporary Excel file
def create_temp_excel_file(file_name, content):
    wb = Workbook()
    ws = wb.active
    for row in content:
        ws.append(row)
    wb.save(file_name)
    return file_name

# Helper function to read CSV file
def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

@pytest.fixture
def setup_files(tmpdir):
    excel_file_path = tmpdir.mkdir("excel")
    csv_file_path = tmpdir.mkdir("csv")
    excel_content = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"]
    ]
    excel_file_name = "test.xlsx"
    excel_file_path = create_temp_excel_file(os.path.join(excel_file_path, excel_file_name), excel_content)
    return excel_file_path, csv_file_path, excel_file_name

def test_task_func(setup_files):
    excel_file_path, csv_file_path, excel_file_name = setup_files
    expected_csv_file_name = os.path.splitext(excel_file_name)[0] + '.csv'
    expected_csv_file_path = os.path.join(csv_file_path, expected_csv_file_name)
    expected_csv_content = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"]
    ]

    result = task_func(excel_file_name, excel_file_path, csv_file_path)
    assert result == expected_csv_file_name

    csv_content = read_csv_file(expected_csv_file_path)
    assert csv_content == expected_csv_content

def test_task_func_nonexistent_file(tmpdir):
    excel_file_path = tmpdir.mkdir("excel")
    csv_file_path = tmpdir.mkdir("csv")
    non_existent_file_name = "non_existent.xlsx"

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(non_existent_file_name, excel_file_path, csv_file_path)
    assert f"No such file or directory: '{os.path.join(excel_file_path, non_existent_file_name)}'" in str(excinfo.value)