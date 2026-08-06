import pytest
from src_0080 import task_func
from django.http import HttpRequest

@pytest.fixture
def request():
    return HttpRequest()

def test_task_func_with_single_file(request):
    file_paths = ['file1.txt']
    response = task_func(request, file_paths)
    
    assert response.status_code == 200
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response['Content-Type'] == 'application/zip'
    
    zip_content = response.content
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        assert 'file1.txt' in zip_file.namelist()
        with zip_file.open('file1.txt') as f:
            assert f.read().decode() == 'This is the content of file1.txt.'

def test_task_func_with_multiple_files(request):
    file_paths = ['file1.txt', 'file2.txt']
    response = task_func(request, file_paths)
    
    assert response.status_code == 200
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response['Content-Type'] == 'application/zip'
    
    zip_content = response.content
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        assert set(zip_file.namelist()) == {'file1.txt', 'file2.txt'}
        with zip_file.open('file1.txt') as f:
            assert f.read().decode() == 'This is the content of file1.txt.'
        with zip_file.open('file2.txt') as f:
            assert f.read().decode() == 'This is the content of file2.txt.'

def test_task_func_with_no_files(request):
    file_paths = []
    response = task_func(request, file_paths)
    
    assert response.status_code == 200
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response['Content-Type'] == 'application/zip'
    
    zip_content = response.content
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        assert zip_file.namelist() == []

def test_task_func_with_empty_string_in_file_paths(request):
    file_paths = ['']
    response = task_func(request, file_paths)
    
    assert response.status_code == 200
    assert response['Content-Disposition'] == 'attachment; filename="files.zip"'
    assert response['Content-Type'] == 'application/zip'
    
    zip_content = response.content
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        assert zip_file.namelist() == ['']
        with zip_file.open('') as f:
            assert f.read().decode() == 'This is the content of .'