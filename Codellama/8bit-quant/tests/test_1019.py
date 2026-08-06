import pytest
from src_1019 import task_func

def test_task_func_with_valid_url():
    url = "http://example.com"
    from_encoding = "cp1251"
    use_lxml = False
    soup = task_func(url, from_encoding, use_lxml)
    assert soup is not None
    assert soup.title.string == "Example Domain"

def test_task_func_with_invalid_url():
    url = "http://example.com/invalid"
    from_encoding = "cp1251"
    use_lxml = False
    soup = task_func(url, from_encoding, use_lxml)
    assert soup is None

def test_task_func_with_invalid_encoding():
    url = "http://example.com"
    from_encoding = "invalid_encoding"
    use_lxml = False
    soup = task_func(url, from_encoding, use_lxml)
    assert soup is None

def test_task_func_with_lxml_parser():
    url = "http://example.com"
    from_encoding = "cp1251"
    use_lxml = True
    soup = task_func(url, from_encoding, use_lxml)
    assert soup is not None
    assert soup.title.string == "Example Domain"
    assert soup.parser == "lxml"