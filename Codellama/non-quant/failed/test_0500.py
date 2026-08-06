import pytest
from src_0500 import task_func

def test_task_func():
    csv_content = "col1,col2,col3\n1,2,3\n4,5,6"
    filename = "test_file.xls"
    expected_path = os.path.abspath(filename)

    result = task_func(csv_content, filename)

    assert result == expected_path

    with open(result, "rb") as f:
        book = xlwt.Workbook(f)
        sheet1 = book.get_sheet(0)

        assert sheet1.get_cell(0, 0).value == "col1"
        assert sheet1.get_cell(0, 1).value == "col2"
        assert sheet1.get_cell(0, 2).value == "col3"
        assert sheet1.get_cell(1, 0).value == "1"
        assert sheet1.get_cell(1, 1).value == "2"
        assert sheet1.get_cell(1, 2).value == "3"
        assert sheet1.get_cell(2, 0).value == "4"
        assert sheet1.get_cell(2, 1).value == "5"
        assert sheet1.get_cell(2, 2).value == "6"