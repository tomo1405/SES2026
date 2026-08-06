import zipfile

from src_0080 import task_func


def test_task_func():
    request = HttpRequest()
    file_paths = ['file1.txt', 'file2.txt']
    response = task_func(request, file_paths)

    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert response['Content-Disposition'] == 'attachment; filename=files.zip'

    zip_file = zipfile.ZipFile(response.file_obj)
    assert zip_file.namelist() == file_paths
    for file_path in file_paths:
        assert zip_file.read(file_path) == 'This is the content of {}.'.format(file_path).encode()