import pytest
from src_0080 import task_func

def test_task_func():
    request = HttpRequest()
    file_paths = ['path1', 'path2', 'path3']

    response = task_func(request, file_paths)

    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert response.get('Content-Disposition') == 'attachment; filename="files.zip"'