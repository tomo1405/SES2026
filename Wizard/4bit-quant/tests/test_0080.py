python
import pytest
from src_0080 import task_func

@pytest.fixture
def request_obj():
    request = HttpRequest()
    request.method = 'GET'
    return request

@pytest.fixture
def file_paths():
    return ['file1.txt', 'file2.txt']

def test_task_func(request_obj, file_paths):
    response = task_func(request_obj, file_paths)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response.content == b'This is the content of file1.txt.\nThis is the content of file2.txt.'