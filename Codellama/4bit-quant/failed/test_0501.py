import pytest
from src_0501 import task_func

def test_task_func():
    values = [
        {'ID': 1, 'Name': 'John Doe', 'Age': 30},
        {'ID': 2, 'Name': 'Jane Doe', 'Age': 25},
        {'ID': 3, 'Name': 'John Smith', 'Age': 40}
    ]
    filename = 'test_data.xls'
    result = task_func(values, filename)
    assert result == os.path.abspath(filename)

    # Check that the file was created and has the correct data
    assert os.path.exists(filename)
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("persons")
    for col_index, col in enumerate(FIELDS):
        assert sheet1.read(0, col_index) == col
    for row_index, row_values in enumerate(values, 1):
        for col_index, col in enumerate(FIELDS):
            value = row_values.get(col, "")
            assert sheet1.read(row_index, col_index) == value

    # Clean up
    os.remove(filename)