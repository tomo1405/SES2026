import pytest
from src_0501 import task_func


def test_task_func():
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 25},
        {'ID': 2, 'Name': 'Jane', 'Age': 30},
        {'ID': 3, 'Name': 'Bob', 'Age': 35},
    ]
    filename = 'test_data.xls'

    result = task_func(values, filename)

    assert os.path.exists(result)
    assert os.path.isfile(result)

    with open(result, 'rb') as f:
        book = xlwt.Workbook(f)
        sheet1 = book.get_sheet(0)

        assert sheet1.name == 'persons'

        for col_index, col in enumerate(FIELDS):
            assert sheet1.cell(0, col_index).value == col

        for row_index, row_values in enumerate(values, 1):
            for col_index, col in enumerate(FIELDS):
                value = row_values.get(col, "")
                assert sheet1.cell(row_index, col_index).value == value