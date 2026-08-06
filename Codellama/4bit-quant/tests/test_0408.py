import pytest
from src_0408 import task_func

def test_task_func():
    # Test if the function raises an error when the Excel file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('test.xlsx', '/path/to/excel/files', '/path/to/csv/files')

    # Test if the function returns the correct CSV file name
    csv_file_name = task_func('test.xlsx', '/path/to/excel/files', '/path/to/csv/files')
    assert csv_file_name == 'test.csv'

    # Test if the function writes the correct data to the CSV file
    csv_file = os.path.join('/path/to/csv/files', csv_file_name)
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    assert data == [['value1', 'value2', 'value3'], ['value4', 'value5', 'value6']]