import pytest
from src_1130 import task_func

def test_task_func():
    json_data = '{"url": "https://www.example.com"}'
    unknown_key = "url"
    save_dir = "./"
    file_path = task_func(json_data, unknown_key, save_dir)
    assert file_path == os.path.join(save_dir, f"{unknown_key}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.txt")
    assert os.path.exists(file_path)
    with open(file_path, 'rb') as f:
        assert f.read() == b'<html><body>Example Domain</body></html>'
    os.remove(file_path)