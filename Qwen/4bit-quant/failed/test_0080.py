import pytest
from src_0080 import task_func
from django.http import HttpRequest

@pytest.mark.django_db
def test_task_func():
    request = HttpRequest()
    file_paths = ['file1.txt', 'file2.txt']

    response = task_func(request, file_paths)

    assert isinstance(response, FileResponse)
    assert response.as_attachment is True
    assert response['Content-Type'] == 'application/zip'
    assert response['Content-Disposition'].startswith('attachment; filename="files.zip"')

    # Check the content of the zip file
    zip_content = response.streaming_content.read()
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        assert set(zip_file.namelist()) == set(file_paths)
        for file_path in file_paths:
            with zip_file.open(file_path) as f:
                content = f.read().decode('utf-8')
                assert content == 'This is the content of {}.'.format(file_path)