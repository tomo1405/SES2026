python
import pytest
from src_0080 import task_func

@pytest.fixture
def request_obj():
    class Request:
        pass
    return Request()

def test_task_func(request_obj):
    file_paths = ['file1.txt', 'file2.txt']
    response = task_func(request_obj, file_paths)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response.content == b'This is the content of file1.txt.\nThis is the content of file2.txt.'