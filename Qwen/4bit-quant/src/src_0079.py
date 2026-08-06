import csv
import io
from django.http import HttpRequest, FileResponse
def task_func(request, header, csv_data):
    csv_io = io.StringIO()
    writer = csv.writer(csv_io)
    writer.writerow(header)
    writer.writerows(csv_data)
    csv_io.seek(0)

    response = FileResponse(csv_io, as_attachment=True, filename='data.csv')
    response['Content-Type'] = 'text/csv'

    return response