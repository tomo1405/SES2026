import pytest
from src_1000 import task_func

def test_task_func():
    url = "https://example.com/data.csv"
    column_name = "age"
    csv_file_path = "data.csv"

    # Test that the function raises a ValueError if the column name is not in the CSV file
    with pytest.raises(ValueError):
        task_func(url, "invalid_column_name", csv_file_path)

    # Test that the function returns a Counter object with the correct values
    counter = task_func(url, column_name, csv_file_path)
    assert isinstance(counter, collections.Counter)
    assert counter[column_name] == 10

    # Test that the function removes the CSV file after it is processed
    assert not os.path.exists(csv_file_path)