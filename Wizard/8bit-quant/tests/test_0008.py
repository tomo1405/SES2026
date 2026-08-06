python
import csv
import collections
import operator
import pytest

def task_func(csv_file_path):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        sales_data = collections.defaultdict(int)
        for row in reader:
            product, quantity = row[0], int(row[1])
            sales_data[product] += quantity

    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]

    return top_selling_product

def test_task_func():
    # Test case 1
    csv_file_path = "test_data.csv"
    expected_result = "Product 2"
    assert task_func(csv_file_path) == expected_result

    # Test case 2
    csv_file_path = "test_data_2.csv"
    expected_result = "Product 1"
    assert task_func(csv_file_path) == expected_result