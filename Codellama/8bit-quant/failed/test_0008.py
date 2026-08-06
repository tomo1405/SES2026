import pytest
from src_0008 import task_func

def test_task_func():
    csv_file_path = 'test_data.csv'
    with open(csv_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Product', 'Quantity'])
        writer.writerow(['Product A', '10'])
        writer.writerow(['Product B', '20'])
        writer.writerow(['Product C', '30'])

    top_selling_product = task_func(csv_file_path)

    assert top_selling_product == 'Product B'