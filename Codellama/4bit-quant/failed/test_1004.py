import pytest
from src_1004 import task_func

def test_task_func():
    # Test with valid URL
    url = "https://www.example.com/data.xml"
    result = task_func(url)
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0

    # Test with invalid URL
    url = "https://www.example.com/invalid.xml"
    with pytest.raises(ValueError):
        task_func(url)

    # Test with invalid XML syntax
    url = "https://www.example.com/data.xml"
    with pytest.raises(ValueError):
        task_func(url)

    # Test with empty XML structure
    url = "https://www.example.com/data.xml"
    with pytest.raises(ValueError):
        task_func(url)