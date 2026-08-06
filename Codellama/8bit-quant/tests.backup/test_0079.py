import pytest
from src_0079 import task_func

def test_task_func():
    request = HttpRequest()
    header = ['Name', 'Age']
    csv_data = [['Alice', 25], ['Bob', 30]]

    response = task_func(request, header, csv_data)

    assert response.status_code == 200
    assert response['Content-Type'] == 'text/csv'
    assert response['Content-Disposition'] == 'attachment; filename="data.csv"'

    csv_io = io.StringIO(response.content.decode('utf-8'))
    reader = csv.reader(csv_io)

    assert next(reader) == header
    assert list(reader) == csv_data