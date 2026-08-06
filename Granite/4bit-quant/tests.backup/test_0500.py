import pytest
from src_0500 import task_func

def test_task_func():
    csv_content = "col1,col2,col3\nrow1,value1,value2\nrow2,value3,value4"
    filename = "test_file.xls"
    result = task_func(csv_content, filename)
    assert result == os.path.abspath(filename)

def test_task_func_with_invalid_csv():
    csv_content = "invalid_csv"
    filename = "test_file.xls"
    with pytest.raises(ValueError):
        task_func(csv_content, filename)