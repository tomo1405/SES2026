python
import pytest
from src_0282 import task_func

def test_task_func():
    folder_path = 'test_folder'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    os.makedirs(folder_path, exist_ok=True)
    with open(os.path.join(folder_path, 'test1.log'), 'w') as file:
        file.write('192.168.1.1 - - [01/Jan/1970:00:00:01 +0000] "GET / HTTP/1.1" 200 1234 "http://example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')
    with open(os.path.join(folder_path, 'test2.log'), 'w') as file:
        file.write('192.168.1.1 - - [01/Jan/1970:00:00:02 +0000] "GET / HTTP/1.1" 200 1234 "http://example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')
    with open(os.path.join(folder_path, 'test3.log'), 'w') as file:
        file.write('192.168.1.2 - - [01/Jan/1970:00:00:01 +0000] "GET / HTTP/1.1" 200 1234 "http://example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')
    result = task_func(folder_path)
    assert result == expected_result
    os.remove(os.path.join(folder_path, 'test1.log'))
    os.remove(os.path.join(folder_path, 'test2.log'))
    os.remove(os.path.join(folder_path, 'test3.log'))
    os.rmdir(folder_path)