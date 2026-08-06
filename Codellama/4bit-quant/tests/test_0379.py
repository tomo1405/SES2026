import pytest
from src_0379 import task_func

def test_task_func():
    # Test that the function raises an error when the data directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(data_dir='/path/to/nonexistent/directory')

    # Test that the function raises an error when there are no CSV files in the data directory
    with pytest.raises(ValueError):
        task_func(data_dir='/path/to/empty/directory')

    # Test that the function returns a valid Texttable object when there are CSV files in the data directory
    table = task_func(data_dir='/path/to/data/directory')
    assert isinstance(table, Texttable)
    assert table.rows[0][0] == 'File'
    assert table.rows[0][1] == 'Rows'
    assert table.rows[0][2] == 'Columns'
    assert len(table.rows) > 1

    # Test that the function handles an empty CSV file correctly
    with pytest.raises(pd.errors.EmptyDataError):
        task_func(data_dir='/path/to/empty/csv/file')