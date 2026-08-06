python
import uuid
from django.http import HttpResponse

def test_task_func():
    data = '{"message": "Hello, world!"}'
    response = task_func(data)
    assert response.content == data
    assert response['UUID'] == str(uuid.uuid4())