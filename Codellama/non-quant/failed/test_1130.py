import pytest
from src_1130 import task_func

def test_task_func():
    json_data = '{"url": "https://www.example.com"}'
    unknown_key = "url"
    save_dir = "./test_data"
    file_path = task_func(json_data, unknown_key, save_dir)
    assert file_path == os.path.join(save_dir, f"{unknown_key}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.txt")
    assert os.path.exists(file_path)
    with open(file_path, 'rb') as f:
        assert f.read() == b'<!DOCTYPE html><html><head><title>Example Domain</title><meta charset="UTF-8"></head><body><div><h1>Example Domain</h1><p>This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.</p><p><a href="https://www.iana.org/domains/example">More information...</a></p></div></body></html>'
    os.remove(file_path)