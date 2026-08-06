import pytest
from src_0501 import task_func

def test_task_func():
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 25},
        {'ID': 2, 'Name': 'Bob', 'Age': 30},
        {'ID': 3, 'Name': 'Charlie', 'Age': 35},
    ]
    filename = 'output.xls'

    result = task_func(values, filename)

    assert result == os.path.abspath(filename)
    assert os.path.exists(filename)

    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name('persons')

    assert sheet.ncols == len(FIELDS)
    assert sheet.nrows == len(values) + 1

    for col_index, col in enumerate(FIELDS):
        assert sheet.cell(0, col_index).value == col

    for row_index, row_values in enumerate(values, 1):
        for col_index, col in enumerate(FIELDS):
            value = row_values.get(col, "")
            assert sheet.cell(row_index, col_index).value == value

    os.remove(filename)