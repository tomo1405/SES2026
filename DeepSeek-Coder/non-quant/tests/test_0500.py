import pytest
from src_0500 import task_func
import os
import io
import csv
import xlwt

def test_task_func():
    # Test data
    csv_content = "col1,col2\nval1,val2"
    filename = "test_output.xls"

    # Call the function
    result = task_func(csv_content=csv_content, filename=filename)

    # Assertions
    assert os.path.exists(result)
    assert os.path.getsize(result) > 0

    # Clean up
    os.remove(result)