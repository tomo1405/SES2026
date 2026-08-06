import pytest
from src_0529 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import csv

def test_task_func_with_no_duplicates():
    # Create a CSV content with no duplicates
    csv_content = """name,age
Alice,30
Bob,25"""

    # Create a BytesIO object to simulate a file
    file_like_object = io.StringIO(csv_content)

    # Use the file-like object in the function
    duplicates, ax = task_func(file_like_object)

    # Check that there are no duplicates
    assert duplicates == Counter()

    # Check that the plot is None since there are no duplicates
    assert ax is None

def test_task_func_with_duplicates():
    # Create a CSV content with duplicates
    csv_content = """name,age
Alice,30
Bob,25
Alice,30"""

    # Create a BytesIO object to simulate a file
    file_like_object = io.StringIO(csv_content)

    # Use the file-like object in the function
    duplicates, ax = task_func(file_like_object)

    # Check that there is one duplicate entry
    assert duplicates == Counter([("Alice", 30)])

    # Check that the plot is not None
    assert ax is not None

def test_task_func_with_invalid_file_format():
    # Test with an invalid file format
    with pytest.raises(ValueError) as excinfo:
        task_func("data.txt")

    # Check the error message
    assert str(excinfo.value) == "Invalid file format. Only .csv files are accepted."

def test_task_func_with_empty_file():
    # Create an empty CSV file
    csv_content = ""

    # Create a BytesIO object to simulate a file
    file_like_object = io.StringIO(csv_content)

    # Use the file-like object in the function
    duplicates, ax = task_func(file_like_object)

    # Check that there are no duplicates
    assert duplicates == Counter()

    # Check that the plot is None since there are no entries
    assert ax is None