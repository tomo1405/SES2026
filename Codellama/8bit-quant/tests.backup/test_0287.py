import pytest
from src_0287 import task_func

def test_task_func():
    output_file = 'test_output.csv'
    test_directory = 'test_files'
    total_words = task_func(output_file, test_directory)
    assert total_words == 10

    with open(output_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows[0] == ['Word', 'Count']
        assert rows[1] == ['hello', '2']
        assert rows[2] == ['world', '3']
        assert rows[3] == ['python', '4']

    os.remove(output_file)