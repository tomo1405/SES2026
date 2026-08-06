import pytest
from src_0408 import task_func
import os
import csv
from openpyxl import Workbook

def test_task_func_valid_excel(tmpdir):
    # Create a temporary Excel file
    excel_file_path = tmpdir.mkdir("excel")
    excel_file_name = "test.xlsx"
    excel_file = excel_file_path.join(excel_file_name)
    
    wb = Workbook()
    ws = wb.active
    ws.append([1, 2, 3])
    ws.append([4, 5, 6])
    wb.save(str(excel_file))

    # Create a temporary CSV directory
    csv_file_path = tmpdir.mkdir("csv")

    # Call the function
    result = task_func(excel_file_name, str(excel_file_path), str(csv_file_path))

    # Check if the CSV file was created
    csv_file = csv_file_path.join(result)
    assert csv_file.exists()

    # Read the CSV file and check its contents
    with open(str(csv_file), 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [[1, 2, 3], [4, 5, 6]]

def test_task_func_nonexistent_excel(tmpdir):
    excel_file_path = tmpdir.mkdir("excel")
    csv_file_path = tmpdir.mkdir("csv")
    excel_file_name = "nonexistent.xlsx"

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(excel_file_name, str(excel_file_path), str(csv_file_path))

    assert str(excinfo.value) == f"[Errno 2] No such file or directory: '{os.path.join(excel_file_path, excel_file_name)}'"

def test_task_func_empty_excel(tmpdir):
    excel_file_path = tmpdir.mkdir("excel")
    csv_file_path = tmpdir.mkdir("csv")
    excel_file_name = "empty.xlsx"
    
    wb = Workbook()
    ws = wb.active
    wb.save(str(excel_file_path.join(excel_file_name)))

    result = task_func(excel_file_name, str(excel_file_path), str(csv_file_path))

    csv_file = csv_file_path.join(result)
    assert csv_file.exists()

    with open(str(csv_file), 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == []

def test_task_func_existing_csv(tmpdir):
    excel_file_path = tmpdir.mkdir("excel")
    csv_file_path = tmpdir.mkdir("csv")
    excel_file_name = "test.xlsx"
    
    wb = Workbook()
    ws = wb.active
    ws.append([1, 2, 3])
    wb.save(str(excel_file_path.join(excel_file_name)))

    # Create an existing CSV file
    csv_file_name = "test.csv"
    csv_file = csv_file_path.join(csv_file_name)
    with open(str(csv_file), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([7, 8, 9])

    result = task_func(excel_file_name, str(excel_file_path), str(csv_file_path))

    csv_file = csv_file_path.join(result)
    assert csv_file.exists()

    with open(str(csv_file), 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [[1, 2, 3]]