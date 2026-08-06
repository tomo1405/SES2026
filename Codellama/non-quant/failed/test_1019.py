import pytest
from src_1019 import task_func

def test_task_func_valid_url():
    url = "http://example.com"
    from_encoding = "cp1251"
    use_lxml = False
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    decoded_content = response.content.decode(from_encoding)
    parser = "lxml" if use_lxml else "html.parser"
    soup = BeautifulSoup(decoded_content, parser)
    assert task_func(url, from_encoding, use_lxml) == soup

def test_task_func_invalid_url():
    url = ""
    from_encoding = "cp1251"
    use_lxml = False
    assert task_func(url, from_encoding, use_lxml) == None

def test_task_func_invalid_encoding():
    url = "http://example.com"
    from_encoding = ""
    use_lxml = False
    assert task_func(url, from_encoding, use_lxml) == None

def test_task_func_invalid_parser():
    url = "http://example.com"
    from_encoding = "cp1251"
    use_lxml = False
    assert task_func(url, from_encoding, use_lxml) == None