python
import csv
import io
from django.http import HttpRequest, FileResponse
import pytest

@pytest.fixture
def request_fixture():
    request = HttpRequest()
    request.method = 'GET'
    return request

@pytest.fixture
def header_fixture():
    return ['Column 1', 'Column 2', 'Column 3']

@pytest.fixture
def csv_data_fixture():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def test_task_func(request_fixture, header_fixture, csv_data_fixture):
    csv_io = io.StringIO()
    writer = csv.writer(csv_io)
    writer.writerow(header_fixture)
    writer.writerows(csv_data_fixture)
    csv_io.seek(0)

    response = FileResponse(csv_io, as_attachment=True, filename='data.csv')
    response['Content-Type'] = 'text/csv'

    assert response.status_code == 200
    assert response['Content-Type'] == 'text/csv'
    assert response['Content-Disposition'] == 'attachment; filename="data.csv"'
    assert response.content == b'Column 1,Column 2,Column 3\n1,2,3\n4,5,6\n7,8,9\n'