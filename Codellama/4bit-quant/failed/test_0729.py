import pytest
from src_0729 import task_func

def test_task_func():
    # Test with a valid filename
    filename = 'test_data.csv'
    from_encoding = 'cp1251'
    to_encoding = 'utf8'
    delimiter = ','
    data, converted_csv = task_func(filename, from_encoding, to_encoding, delimiter)
    assert data == [{'Column': 'Value'}]
    assert converted_csv == 'Column,Value\n'

    # Test with a non-existent filename
    filename = 'non_existent_file.csv'
    with pytest.raises(FileNotFoundError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a non-CSV file
    filename = 'test_data.txt'
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a non-existent encoding
    filename = 'test_data.csv'
    from_encoding = 'non_existent_encoding'
    to_encoding = 'utf8'
    with pytest.raises(LookupError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a non-existent delimiter
    filename = 'test_data.csv'
    from_encoding = 'cp1251'
    to_encoding = 'utf8'
    delimiter = '|'
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding, delimiter)