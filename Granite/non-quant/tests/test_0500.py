import os

from src_0500 import task_func


def test_task_func():
    csv_content = "col1,col2,col3nval1,val2,val3nval4,val5,val6"
    filename = "test_file.xls"

    result = task_func(csv_content, filename)

    assert result == os.path.abspath(filename)
    assert os.path.exists(filename)  # Check if the file was created

    # Cleanup
    os.remove(filename)