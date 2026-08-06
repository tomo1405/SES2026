import pytest
from src_0375 import task_func


def test_task_func_valid_directory():
    directory_path = './xlsx_files/'
    processed_files = task_func(directory_path)
    assert processed_files > 0

def test_task_func_invalid_directory():
    directory_path = './invalid_directory/'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)

def test_task_func_valid_xlsx_file():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_invalid_xlsx_file():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'invalid_file.xlsx'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)

def test_task_func_valid_sheet():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_invalid_sheet():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = 'invalid_sheet'
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_valid_row():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_invalid_row():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_valid_cell():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1

def test_task_func_invalid_cell():
    directory_path = './xlsx_files/'
    xlsx_file = directory_path + 'test_file.xlsx'
    workbook = load_workbook(filename=xlsx_file)
    sheet = workbook.sheetnames[0]
    row = workbook[sheet].iter_rows()[0]
    cell = row[0]
    cell.value = 'test_value'
    workbook.save(xlsx_file)
    processed_files = task_func(directory_path)
    assert processed_files == 1