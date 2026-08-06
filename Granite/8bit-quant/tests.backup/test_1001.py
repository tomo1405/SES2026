import pytest
from src_1001 import task_func

def test_task_func():
    # Test case 1: Test with a valid URL
    url = "https://example.com/data.json"
    expected_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    actual_df = task_func(url)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with an invalid URL
    url = "https://example.com/invalid_file.json"
    with pytest.raises(Exception) as exc_info:
        task_func(url)
    assert "Failed to retrieve data from the URL" in str(exc_info.value)