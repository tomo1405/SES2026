import pytest
from src_0080 import task_func
from unittest.mock import patch
from django.http import HttpRequest

@pytest.fixture
def request_mock():
    request = HttpRequest()
    request.method = 'GET'
    request.path = '/some-path'
    request.META = {'HTTP_HOST': 'testserver'}
    return request

def test_task_func(request_mock):
    file_paths = ['file1.txt', 'file2.txt']
    response = task_func(request_mock, file_paths)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/zip'
    assert 'attachment; filename=files.zip' in response['Content-Disposition']