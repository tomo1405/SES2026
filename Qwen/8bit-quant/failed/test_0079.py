import pytest
from django.http import HttpRequest
from src_0079 import task_func

@pytest.fixture
def request():
    return HttpRequest()

@pytest.fixture
def header():
    return ['Name', 'Age', 'City']

@pytest.fixture
def csv_data():
    return [
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]

def test_task_func(request, header, csv_data):
    response = task_func(request, header, csv_data)
    
    assert isinstance(response, FileResponse)
    assert response['Content-Disposition'] == 'attachment; filename="data.csv"'
    assert response['Content-Type'] == 'text/csv'
    
    # Read the content of the response
    response.seek(0)
    content = response.read().decode('utf-8')
    
    # Expected CSV content
    expected_content = (
        'Name,Age,City\r\n'
        'Alice,30,New York\r\n'
        'Bob,25,Los Angeles\r\n'
        'Charlie,35,Chicago\r\n'
    )
    
    assert content == expected_content