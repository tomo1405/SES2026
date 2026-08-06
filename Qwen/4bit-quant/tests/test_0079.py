import pytest
from django.http import HttpRequest
from src_0079 import task_func

def test_task_func():
    request = HttpRequest()
    header = ['Name', 'Age', 'City']
    csv_data = [
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles']
    ]

    response = task_func(request, header, csv_data)

    assert isinstance(response, FileResponse)
    assert response['Content-Type'] == 'text/csv'
    assert response['Content-Disposition'] == 'attachment; filename="data.csv"'

    # Read the content of the response
    response.seek(0)
    content = response.read().decode('utf-8')

    # Check the CSV content
    expected_content = "Name,Age,City\nAlice,30,New York\nBob,25,Los Angeles\n"
    assert content == expected_content