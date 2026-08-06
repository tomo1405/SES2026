import pytest
from src_0729 import task_func


def test_task_func():
    # Test with a valid filename
    filename = 'test_data.csv'
    from_encoding = 'cp1251'
    to_encoding = 'utf8'
    delimiter = ','
    data, converted_csv = task_func(filename, from_encoding, to_encoding, delimiter)
    assert data is not None
    assert converted_csv is not None

    # Test with a non-existent filename
    filename = 'non_existent_file.csv'
    with pytest.raises(FileNotFoundError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a filename that is not a CSV file
    filename = 'test_data.txt'
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a filename that has invalid encoding
    filename = 'test_data.csv'
    from_encoding = 'invalid_encoding'
    with pytest.raises(LookupError):
        task_func(filename, from_encoding, to_encoding, delimiter)

    # Test with a filename that has invalid delimiter
    filename = 'test_data.csv'
    delimiter = 'invalid_delimiter'
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding, delimiter)