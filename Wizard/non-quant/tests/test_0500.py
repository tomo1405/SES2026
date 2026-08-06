python
import pytest
from src_0500 import task_func

def test_task_func():
    csv_content = "1,2,3\n4,5,6"
    filename = "test.xls"
    result = task_func(csv_content, filename)
    assert result == os.path.abspath(filename)