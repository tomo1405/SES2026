import pytest
from src_0008 import task_func

def test_task_func():
    csv_file_path = "test_data.csv"
    with open(csv_file_path, 'w') as f:
        f.write("Product,Quantity\n")
        f.write("Product A,10\n")
        f.write("Product B,20\n")
        f.write("Product C,30\n")

    top_selling_product = task_func(csv_file_path)

    assert top_selling_product == "Product B"