import pytest
from src_0184 import task_func
from django.http import HttpResponse
import uuid

def test_task_func():
    data = "example data"
    response = task_func(data)
    assert isinstance(response, HttpResponse)
    assert response.content == data.encode('utf-8')
    assert response['Content-Type'] == 'application/json'
    assert response['UUID'] == str(uuid.uuid4())