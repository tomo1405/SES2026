import pytest
from src_0080 import task_func
from django.http import HttpRequest

def test_task_func():
    request = HttpRequest()
    file_paths = ['file1.txt', 'file2.txt']
    response = task_func(request, file_paths)

    assert isinstance(response, FileResponse)
    assert response['Content-Type'] == 'application/zip'
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'

    # Check the content of the zip file
    zip_content = response.streaming_content
    with zipfile.ZipFile(io.BytesIO(b''.join(zip_content))) as zip_file:
        assert zip_file.namelist() == file_paths
        for file_path in file_paths:
            with zip_file.open(file_path) as f:
                content = f.read().decode('utf-8')
                assert content == 'This is the content of {}.'.format(file_path)