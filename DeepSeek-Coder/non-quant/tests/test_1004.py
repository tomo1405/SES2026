import pytest
from src_1004 import task_func

def test_task_func_valid_xml():
    url = "https://example.com/valid_xml"
    result = task_func(url)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"

def test_task_func_invalid_xml():
    url = "https://example.com/invalid_xml"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_network_error():
    url = "https://invalid-url"
    with pytest.raises(ValueError):
        task_func(url)