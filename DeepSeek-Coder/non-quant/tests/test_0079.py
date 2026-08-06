import pytest
from src_0079 import task_func
from unittest.mock import patch
from io import StringIO
import csv
from django.http import HttpRequest

@pytest.fixture
def request_mock():
    req = HttpRequest()
    req.method = 'GET'
    return req

@pytest.fixture
def header():
    return ['header1', 'header2']

@pytest.fixture
def csv_data():
    return [['data1', 'data2'], ['data3', 'data4']]

def test_task_func(request_mock, header, csv_data):
    response = task_func(request_mock, header, csv_data)
    assert response.status_code == 200
    assert response['Content-Type'] == 'text/csv'
    assert response.get('Content-Disposition') == 'attachment; filename=data.csv'
    csv_io = StringIO(response.content)
    reader = csv.reader(csv_io)
    assert list(reader) == header + csv_data