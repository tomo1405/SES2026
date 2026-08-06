import pytest
from src_0079 import task_func

def test_task_func():
    request = HttpRequest()
    header = ['Name', 'Age', 'Gender']
    csv_data = [['John', 25, 'Male'], ['Jane', 30, 'Female']]

    response = task_func(request, header, csv_data)

    assert response.status_code == 200
    assert response['Content-Type'] == 'text/csv'
    assert response.get('Content-Disposition') == 'attachment; filename="data.csv"'