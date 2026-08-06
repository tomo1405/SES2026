from src_0080 import task_func


def test_task_func():
    request = HttpRequest()
    file_paths = ['path1.txt', 'path2.txt', 'path3.txt']

    response = task_func(request, file_paths)

    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert response.getvalue() == b'This is the content of path1.txt.This is the content of path2.txt.This is the content of path3.txt.'