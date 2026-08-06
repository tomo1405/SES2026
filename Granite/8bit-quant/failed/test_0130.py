import pytest
from src_0130 import task_func

def test_task_func():
    # Test case 1: Valid URL, valid table and data
    df = task_func('http://example.com')
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0  # Check if the DataFrame is not empty
    assert df.shape[1] > 0  # Check if the DataFrame has at least one column

    # Test case 2: Valid URL, no table found
    with pytest.raises(ValueError) as excinfo:
        task_func('http://example.com/invalid-page')
    assert "No table found on the page." in str(excinfo.value)

    # Test case 3: Invalid URL, connection error
    with pytest.raises(ConnectionError) as excinfo:
        task_func('http://invalid-url.com')
    assert "Could not connect to URL" in str(excinfo.value)

    # Test case 4: Valid URL, valid table, but no data
    with pytest.raises(ValueError) as excinfo:
        task_func('http://example.com/empty-table')
    assert "No data found in the table." in str(excinfo.value)