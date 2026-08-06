import pytest
from src_0729 import task_func

def test_task_func_default_encoding():
    # Create a CSV file with cp1251 encoding
    input_csv = u"Name,Age\nIvan,30\nPetr,25"
    input_file = io.StringIO(input_csv.encode('cp1251'))
    input_file.name = 'test.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name)

    # Expected output
    expected_data = [{'Name': 'Ivan', 'Age': '30'}, {'Name': 'Petr', 'Age': '25'}]
    expected_csv = "Name,Age\nIvan,30\nPetr,25\n"

    # Assert the results
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_custom_encoding():
    # Create a CSV file with a custom encoding
    input_csv = u"Name,Age\nIvan,30\nPetr,25"
    input_file = io.StringIO(input_csv.encode('latin1'))
    input_file.name = 'test.csv'

    # Call the function with custom encodings
    data, converted_csv = task_func(input_file.name, from_encoding='latin1', to_encoding='utf8')

    # Expected output
    expected_data = [{'Name': 'Ivan', 'Age': '30'}, {'Name': 'Petr', 'Age': '25'}]
    expected_csv = "Name,Age\nIvan,30\nPetr,25\n"

    # Assert the results
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_custom_delimiter():
    # Create a CSV file with a custom delimiter
    input_csv = u"Name;Age\nIvan;30\nPetr;25"
    input_file = io.StringIO(input_csv.encode('cp1251'))
    input_file.name = 'test.csv'

    # Call the function with custom delimiter
    data, converted_csv = task_func(input_file.name, delimiter=';')

    # Expected output
    expected_data = [{'Name': 'Ivan', 'Age': '30'}, {'Name': 'Petr', 'Age': '25'}]
    expected_csv = "Name;Age\nIvan;30\nPetr;25\n"

    # Assert the results
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_no_fieldnames():
    # Create a CSV file without headers
    input_csv = u"Ivan,30\nPetr,25"
    input_file = io.StringIO(input_csv.encode('cp1251'))
    input_file.name = 'test.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name)

    # Expected output
    expected_data = [{'Column': 'Ivan', 'Column1': '30'}, {'Column': 'Petr', 'Column1': '25'}]
    expected_csv = "Column,Column1\nIvan,30\nPetr,25\n"

    # Assert the results
    assert data == expected_data
    assert converted_csv == expected_csv