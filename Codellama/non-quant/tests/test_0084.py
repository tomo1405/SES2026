import pytest
from src_0084 import task_func

def test_task_func():
    app = task_func('smtp.gmail.com', 587, 'username', 'password', 'templates')
    client = app.test_client()

    response = client.get('/send_mail')
    assert response.status_code == 200
    assert response.data == b'Mail sent!'