import pytest
from src_0389 import task_func

# Example usage:
# my_tuple = ('column1', 'column2')
# path_csv_files = ['file1.csv', 'file2.csv']
# result = task_func(my_tuple, path_csv_files)

@pytest.fixture
def example_data():
    return ({'column1': collections.Counter({'a': 2, 'b': 1}), 'column2': collections.Counter({'c': 3, 'd': 2})}, ['file1.csv', 'file2.csv']

def test_task_func(example_data):
    result = task_func(('column1', 'column2'), ['file1.csv', 'file2.csv'])
    assert result == example_data