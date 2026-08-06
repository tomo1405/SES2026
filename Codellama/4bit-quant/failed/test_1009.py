import pytest
from src_1009 import task_func

def test_task_func():
    url = "https://www.example.com"
    table_id = "table_id"

    # Test with valid URL and table ID
    df = task_func(url, table_id)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    # Test with invalid URL
    with pytest.raises(requests.exceptions.HTTPError):
        task_func("invalid_url", table_id)

    # Test with invalid table ID
    with pytest.raises(ValueError):
        task_func(url, "invalid_table_id")

    # Test with empty table
    df = task_func(url, table_id)
    assert isinstance(df, pd.DataFrame)
    assert df.empty