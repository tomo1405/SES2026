import pytest
from src_0500 import task_func

def test_task_func():
    csv_content = "col1,col2\nval1,val2\nval3,val4"
    filename = "test_file.xls"
    expected_output = "col1,col2\nval1,val2\nval3,val4"

    output = task_func(csv_content, filename)

    assert output == expected_output