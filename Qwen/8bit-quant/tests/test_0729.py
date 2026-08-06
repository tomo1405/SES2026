import io

from src_0729 import task_func


def test_task_func_with_valid_file():
    # Create a CSV file in cp1251 encoding
    input_data = u"Name,Age\nJohn,30\nJane,25"
    input_file = io.StringIO(input_data.encode('cp1251').decode('latin1'))
    input_file.name = 'test.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name, from_encoding='cp1251', to_encoding='utf8')

    # Expected results
    expected_data = [{'Name': 'John', 'Age': '30'}, {'Name': 'Jane', 'Age': '25'}]
    expected_csv = "Name,Age\nJohn,30\nJane,25\n"

    # Assertions
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_with_missing_fieldnames():
    # Create a CSV file without headers in cp1251 encoding
    input_data = u"John,30\nJane,25"
    input_file = io.StringIO(input_data.encode('cp1251').decode('latin1'))
    input_file.name = 'test_no_headers.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name, from_encoding='cp1251', to_encoding='utf8')

    # Expected results
    expected_data = [{'Column': 'John,30'}, {'Column': 'Jane,25'}]
    expected_csv = "Column\nJohn,30\nJane,25\n"

    # Assertions
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_with_different_delimiter():
    # Create a CSV file with semicolon delimiter in cp1251 encoding
    input_data = u"Name;Age\nJohn;30\nJane;25"
    input_file = io.StringIO(input_data.encode('cp1251').decode('latin1'))
    input_file.name = 'test_semicolon.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name, from_encoding='cp1251', to_encoding='utf8', delimiter=';')

    # Expected results
    expected_data = [{'Name': 'John', 'Age': '30'}, {'Name': 'Jane', 'Age': '25'}]
    expected_csv = "Name;Age\nJohn;30\nJane;25\n"

    # Assertions
    assert data == expected_data
    assert converted_csv == expected_csv

def test_task_func_with_empty_file():
    # Create an empty CSV file in cp1251 encoding
    input_data = u""
    input_file = io.StringIO(input_data.encode('cp1251').decode('latin1'))
    input_file.name = 'empty.csv'

    # Call the function
    data, converted_csv = task_func(input_file.name, from_encoding='cp1251', to_encoding='utf8')

    # Expected results
    expected_data = []
    expected_csv = ""

    # Assertions
    assert data == expected_data
    assert converted_csv == expected_csv