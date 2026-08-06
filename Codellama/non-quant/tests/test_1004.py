import pandas as pd
import pytest
from src_1004 import task_func


def test_task_func_valid_url():
    url = "https://www.example.com/data.xml"
    expected_data = pd.DataFrame({"name": ["John", "Jane"], "age": [25, 30]})
    result = task_func(url)
    assert result.equals(expected_data)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid.xml"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_invalid_xml_syntax():
    url = "https://www.example.com/invalid_syntax.xml"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_empty_xml():
    url = "https://www.example.com/empty.xml"
    with pytest.raises(ValueError):
        task_func(url)