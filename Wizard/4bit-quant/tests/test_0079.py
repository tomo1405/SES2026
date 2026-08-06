python
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request: HttpRequest, header: list, csv_data: list) -> FileResponse:
    csv_io = io.StringIO()
    writer = csv.writer(csv_io)
    writer.writerow(header)
    writer.writerows(csv_data)
    csv_io.seek(0)

    response = FileResponse(csv_io, as_attachment=True, filename='data.csv')
    response['Content-Type'] = 'text/csv'

    return response

def test_task_func():
    request = HttpRequest()
    header = ['Name', 'Age', 'Gender']
    csv_data = [
        ['John', '30', 'Male'],
        ['Jane', '25', 'Female'],
        ['Bob', '40', 'Male']
    ]
    response = task_func(request, header, csv_data)
    assert response.status_code == 200
    assert response['Content-Type'] == 'text/csv'
    assert response['Content-Disposition'] == 'attachment; filename="data.csv"'
    assert response.getvalue().decode('utf-8') == 'Name,Age,Gender\r\nJohn,30,Male\r\nJane,25,Female\r\nBob,40,Male\r\n'